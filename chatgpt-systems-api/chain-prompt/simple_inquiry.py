from utilities import *
from context_setup import *
from all_products import *

user_message_1 = f"""
 tell me about the smartx pro phone and
 the fotosnap camera, the dslr one.
 Also tell me about your tvs """

messages =  [  
{'role':'system', 
 'content': system_message},    
{'role':'user', 
 'content': f"{delimiter}{user_message_1}{delimiter}"},  
] 
category_and_product_response_1 = get_completion_from_messages(messages)
print(category_and_product_response_1)
category_and_product_list = read_string_to_list(category_and_product_response_1)
product_information_for_user_message_1 = generate_output_string(category_and_product_list)

system_message = f"""
You are a customer service assistant for a
large electronic store.
Respond in a friendly and helpful tone,
with very concise answers.
Make sure to ask the user relevant follow up questions.
"""
messages =  [  
{'role':'system',
 'content': system_message},   
{'role':'user',
 'content': user_message_1},  
{'role':'assistant',
 'content': f"""Relevant product information:\n
 {product_information_for_user_message_1}"""},   
]
final_response = get_completion_from_messages(messages)
print(final_response)

