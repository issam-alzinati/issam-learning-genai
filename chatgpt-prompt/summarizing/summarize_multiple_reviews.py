from utilities import *
from product_reviews import *

for i in range(len(reviews)):
    prompt = f"""
    Your task is to generate a short summary of a product
    review from an ecommerce site. 

    Summarize the review below, delimited by triple
    backticks in at most 20 words. 

    Review: ```{reviews[i]}```
    """

    response = get_completion(prompt)
    print(i, response, "\n")
