from process_products import *
from all_products import *

products_and_category = get_products_and_category_json()

customer_msg_0 = f"""Which TV can I buy if I'm on a budget?"""

products_by_category_0 = find_category_and_product_v1(customer_msg_0,
                                                      products_and_category)
print(f"""{bcolors.OKGREEN}{customer_msg_0}{bcolors.ENDC}""")
print(products_by_category_0)

customer_msg_2 = f"""
What computers do you have?"""

products_by_category_2 = find_category_and_product_v1(customer_msg_2,
                                                      products_and_category)
print(f"""{bcolors.OKGREEN}{customer_msg_2}{bcolors.ENDC}""")
print(products_by_category_2)

customer_msg_3 = f"""
tell me about the smartx pro phone and the fotosnap camera, the dslr one.
Also, what TVs do you have?"""

products_by_category_3 = find_category_and_product_v1(customer_msg_3,
                                                      products_and_category)
print(f"""{bcolors.OKGREEN}{customer_msg_3}{bcolors.ENDC}""")
print(products_by_category_3)

customer_msg_4 = f"""
tell me about the CineView TV, the 8K one, Gamesphere console, the X one.
I'm on a budget, what computers do you have?"""

products_by_category_4 = find_category_and_product_v1(customer_msg_4,
                                                      products_and_category)
print(f"""{bcolors.OKGREEN}{customer_msg_4}{bcolors.ENDC}""")
print(products_by_category_4)
