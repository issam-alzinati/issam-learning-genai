from utilities import *
from product_reviews import *

prompt = f"""
Your task is to extract only relevant information from 
a product review from an ecommerce site to give
feedback to the Shipping department. 

From the review below, delimited by triple quotes
extract the information relevant to shipping and 
delivery. Limit to 30 words. 

Review: ```{prod_review}```
"""

response = get_completion(prompt)
print(response)