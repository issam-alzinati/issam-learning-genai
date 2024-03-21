from utilities import *
from product_reviews import *

prompt = f"""
Your task is to generate a short summary of a product
review from an ecommerce site. 

Summarize the review below, delimited by triple 
backticks, in at most 250 characters. 

Review: ```{prod_review}```
"""

response = get_completion(prompt)
print(f"{bcolors.OKGREEN}Limit by 250 characters: {len(response)}{bcolors.ENDC}")
print(response)

prompt1 = f"""
Your task is to generate a short summary of a product
review from an ecommerce site. 

Summarize the review below, delimited by triple 
backticks, in at most 30 words. 

Review: ```{prod_review}```
"""

response1 = get_completion(prompt1)
print(f"{bcolors.OKGREEN}Limit by 30 words: {len(response1.split())}{bcolors.ENDC}")
print(response1)

prompt2 = f"""
Your task is to generate a short summary of a product
review from an ecommerce site. 

Summarize the review below, delimited by triple 
backticks, in at most 2 sentences. 

Review: ```{prod_review}```
"""

response2 = get_completion(prompt2)
print(f"{bcolors.OKGREEN}Limit by 2 sentences{bcolors.ENDC}")
print(response2)