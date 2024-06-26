from utilities import *
from all_products import *
from process_products import *


def process_user_message(user_input="", all_messages=[], debug=True):
    delimiter = "```"
    
    # Step 1: Check input to see if it flags the Moderation API or is a prompt injection
    response = client.moderations.create(input=user_input)
    moderation_output = response.results[0]

    if moderation_output.flagged:
        print("Step 1: Input flagged by Moderation API.")
        return "Sorry, we cannot process this request.", all_messages

    if debug: print("Step 1: Input passed moderation check.")
    
    category_and_product_response = find_category_and_product_only(user_input, get_products_and_category())
    #print(category_and_product_response)
    # Step 2: Extract the list of products
    category_and_product_list = read_string_to_list(category_and_product_response)
    #print(category_and_product_list)

    if debug: print("Step 2: Extracted list of products.")

    # Step 3: If products are found, look them up
    product_information = generate_output_string(category_and_product_list)
    if debug: print("Step 3: Looked up product information.")

    # Step 4: Answer the user question
    system_message = f"""
    You are a customer service assistant for a large electronic store.
    Respond in a friendly and helpful tone, with concise answers.
    Make sure to ask the user relevant follow-up questions.
    """
    messages = [
        {'role': 'system', 'content': system_message},
        {'role': 'user', 'content': f"{delimiter}{user_input}{delimiter}"},
        {'role': 'assistant', 'content': f"Relevant product information:\n{product_information}"}
    ]

    final_response = get_completion_from_messages(all_messages + messages)
    if debug:print("Step 4: Generated response to user question.")
    #print(messages[1:])
    all_messages = all_messages + messages[1:]

    # Step 5: Put the answer through the Moderation API
    response = client.moderations.create(input=final_response)
    moderation_output = response.results[0]

    if moderation_output.flagged:
        if debug: print("Step 5: Response flagged by Moderation API.")
        return "Sorry, we cannot provide this information.", all_messages

    if debug: print("Step 5: Response passed moderation check.")

    # Step 6: Ask the model if the response answers the initial user query well
    user_message = f"""
    Customer message: {delimiter}{user_input}{delimiter}
    Agent response: {delimiter}{final_response}{delimiter}

    Does the response sufficiently answer the question?
    """
    messages = [
        {'role': 'system', 'content': system_message},
        {'role': 'user', 'content': user_message}
    ]
    evaluation_response = get_completion_from_messages(messages)
    if debug: print("Step 6: Model evaluated the response.")

    # Step 7: If yes, use this answer; if not, say that you will connect the user to a human
    if "Y" in evaluation_response:  # Using "in" instead of "==" to be safer for model output variation (e.g., "Y." or "Yes")
        if debug: print("Step 7: Model approved the response.")
        return final_response, all_messages
    else:
        if debug: print("Step 7: Model disapproved the response.")
        neg_str = "I'm unable to provide the information you're looking for. I'll connect you with a human representative for further assistance."
        return neg_str, all_messages
