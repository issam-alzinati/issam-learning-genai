from test_set_and_evaluation import *
from process_products import *

products_and_category = get_products_and_category_json()

score_accum = test_set_evaluation_score(products_and_category,find_category_and_product_v3)
n_examples = len(msg_ideal_pairs_set)
fraction_correct = score_accum / n_examples
print(f"{bcolors.OKGREEN}Fraction correct out of {n_examples}: {fraction_correct}{bcolors.ENDC}")
