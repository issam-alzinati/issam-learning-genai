from utilities import *
from all_products import *
from process_products import *

def eval_with_rubric(test_set, assistant_answer):

    cust_msg = test_set['customer_msg']
    context = test_set['context']
    completion = assistant_answer
    
    system_message = """\
    You are an assistant that evaluates how well the customer service agent \
    answers a user question by looking at the context that the customer service \
    agent is using to generate its response. 
    """

    user_message = f"""\
You are evaluating a submitted answer to a question based on the context \
that the agent uses to answer the question.
Here is the data:
    [BEGIN DATA]
    ************
    [Question]: {cust_msg}
    ************
    [Context]: {context}
    ************
    [Submission]: {completion}
    ************
    [END DATA]

Compare the factual content of the submitted answer with the context. \
Ignore any differences in style, grammar, or punctuation.
Answer the following questions:
    - Is the Assistant response based only on the context provided? (Y or N)
    - Does the answer include information that is not provided in the context? (Y or N)
    - Is there any disagreement between the response and the context? (Y or N)
    - Count how many questions the user asked. (output a number)
    - For each question that the user asked, is there a corresponding answer to it?
      Question 1: (Y or N)
      Question 2: (Y or N)
      ...
      Question N: (Y or N)
    - Of the number of questions asked, how many of these questions were addressed by the answer? (output a number)
"""

    messages = [
        {'role': 'system', 'content': system_message},
        {'role': 'user', 'content': user_message}
    ]

    response = get_completion_from_messages(messages)
    return response


customer_msg = f"""
tell me about the smartx pro phone and the fotosnap camera, the dslr one.
Also, what TVs or TV related products do you have?"""
# customer_msg = f"""What could be a good present for my videographer friend?"""
# customer_msg = f"""I need a charger for my smartphone""

products_by_category = find_category_and_product_v3(customer_msg, get_products_and_category())
category_and_product_list = read_string_to_list(products_by_category)
product_info = generate_output_string(category_and_product_list)
assistant_answer = answer_user_msg(user_msg=customer_msg, product_info=product_info)

cust_prod_info = {
    'customer_msg': customer_msg,
    'context': product_info
}
evaluation_output = eval_with_rubric(cust_prod_info, assistant_answer)
print(f'{bcolors.HEADER}{customer_msg}{bcolors.ENDC}')
print(f'{bcolors.OKCYAN}{assistant_answer}{bcolors.ENDC}')
print(f'{bcolors.OKGREEN}{evaluation_output}{bcolors.ENDC}')