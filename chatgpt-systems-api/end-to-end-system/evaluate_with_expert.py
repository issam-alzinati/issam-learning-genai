from utilities import *
from all_products import *
from process_products import *

test_set_ideal = {
    'customer_msg': """\
tell me about the smartx pro phone and the fotosnap camera, the dslr one.
Also, what TVs or TV related products do you have?""",
    'ideal_answer':"""\
Of course!  The SmartX ProPhone is a powerful
smartphone with advanced camera features.
For instance, it has a 12MP dual camera.
Other features include 5G wireless and 128GB storage.
It also has a 6.1-inch display.  The price is $899.99.

The FotoSnap DSLR Camera is great for
capturing stunning photos and videos.
Some features include 1080p video,
3-inch LCD, a 24.2MP sensor,
and interchangeable lenses.
The price is 599.99.

For TVs and TV related products, we offer 3 TVs


All TVs offer HDR and Smart TV.

The CineView 4K TV has vibrant colors and smart features.
Some of these features include a 55-inch display,
'4K resolution. It's priced at 599.

The CineView 8K TV is a stunning 8K TV.
Some features include a 65-inch display and
8K resolution.  It's priced at 2999.99

The CineView OLED TV lets you experience vibrant colors.
Some features include a 55-inch display and 4K resolution.
It's priced at 1499.99.

We also offer 2 home theater products, both which include bluetooth.
The SoundMax Home Theater is a powerful home theater system for
an immmersive audio experience.
Its features include 5.1 channel, 1000W output, and wireless subwoofer.
It's priced at 399.99.

The SoundMax Soundbar is a sleek and powerful soundbar.
It's features include 2.1 channel, 300W output, and wireless subwoofer.
It's priced at 199.99

Are there any questions additional you may have about these products
that you mentioned here?
Or may do you have other questions I can help you with?
    """
}

def eval_vs_ideal(test_set, assistant_answer):

    cust_msg = test_set['customer_msg']
    ideal = test_set['ideal_answer']
    completion = assistant_answer
    
    system_message = """\
    You are an assistant that evaluates how well the customer service agent \
    answers a user question by comparing the response to the ideal (expert) response
    Output a single letter and nothing else. 
    """

    user_message = f"""\
You are comparing a submitted answer to an expert answer on a given question. Here is the data:
    [BEGIN DATA]
    ************
    [Question]: {cust_msg}
    ************
    [Expert]: {ideal}
    ************
    [Submission]: {completion}
    ************
    [END DATA]

Compare the factual content of the submitted answer with the expert answer. Ignore any differences in style, grammar, or punctuation.
    The submitted answer may either be a subset or superset of the expert answer, or it may conflict with it. Determine which case applies. Answer the question by selecting one of the following options:
    (A) The submitted answer is a subset of the expert answer and is fully consistent with it.
    (B) The submitted answer is a superset of the expert answer and is fully consistent with it.
    (C) The submitted answer contains all the same details as the expert answer.
    (D) There is a disagreement between the submitted answer and the expert answer.
    (E) The answers differ, but these differences don't matter from the perspective of factuality.
  choice_strings: ABCDE
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

products_by_category = find_category_and_product_v3(customer_msg, get_products_and_category())
category_and_product_list = read_string_to_list(products_by_category)
product_info = generate_output_string(category_and_product_list)
assistant_answer = answer_user_msg(user_msg=customer_msg, product_info=product_info)

evaluation_output = eval_vs_ideal(test_set_ideal, assistant_answer)
print(f'{bcolors.HEADER}{customer_msg}{bcolors.ENDC}')
print(f'{bcolors.OKCYAN}{assistant_answer}{bcolors.ENDC}')
print(f'{bcolors.OKGREEN}{evaluation_output}{bcolors.ENDC}')