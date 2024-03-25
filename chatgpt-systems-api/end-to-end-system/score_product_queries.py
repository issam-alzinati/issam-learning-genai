from test_set_and_evaluation import *
from process_products import *

products_and_category = get_products_and_category_json()

print(f'Customer message: {msg_ideal_pairs_set[0]["customer_msg"]}')
print(f'Ideal answer: {msg_ideal_pairs_set[0]["ideal_answer"]}')

response = find_category_and_product_v3(msg_ideal_pairs_set[0]["customer_msg"],
                                         products_and_category)
print(f'Resonse: {response}')

score_v0 = eval_response_with_ideal(response,
                              msg_ideal_pairs_set[0]["ideal_answer"])
print(f'Score: {score_v0}')

print(f'\n')

print(f'Customer message: {msg_ideal_pairs_set[8]["customer_msg"]}')
print(f'Ideal answer: {msg_ideal_pairs_set[8]["ideal_answer"]}')

response = find_category_and_product_v3(msg_ideal_pairs_set[8]["customer_msg"],
                                         products_and_category)
print(f'Response: {response}')

score_v8 = eval_response_with_ideal(response,
                              msg_ideal_pairs_set[8]["ideal_answer"])
print(f'Score: {score_v8}')
