from utilities import *
from product_reviews import *

prompt = f"""
Your task is to generate a short summary of a product
review from an ecommerce site to give feedback to the
pricing department, responsible for determining the
price of the product.  

Summarize the review below, delimited by triple 
backticks, in at most 30 words, and focusing on any aspects
that are relevant to the price and perceived value. 

Review: ```{prod_review}```
"""

response = get_completion(prompt)
print(response)
