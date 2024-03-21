from utilities import *
from product_reviews import *

prompt = f"""
Your task is to generate a short summary of a product
review from an ecommerce site to give feedback to the
Shipping department. 

Summarize the review below, delimited by triple 
backticks, in at most 30 words, and focusing on any aspects
that mention shipping and delivery of the product. 

Review: ```{prod_review}```
"""

response = get_completion(prompt)
print(response)
