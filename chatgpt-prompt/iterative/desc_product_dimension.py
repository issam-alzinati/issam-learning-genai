from utilities import *
from fact_sheet_chair import *

prompt = f"""
Your task is to help a marketing team create a 
description for a retail website of a product based 
on a technical fact sheet.

Write a product description based on the information 
provided in the technical specifications delimited by 
triple backticks.

The description is intended for furniture retailers, 
so should be technical in nature and focus on the 
materials the product is constructed from.

At the end of the description, include every 7-character 
Product ID in the technical specification.

This description should be at most 50 words.

After the description, include a table that gives the 
product's dimensions. The table should have two columns.
In the first column include the name of the dimension. 
In the second column include the measurements in inches only.

Give the table the title 'Product Dimensions'.

Technical specifications: ```{fact_sheet_chair}```
"""

response = get_completion(prompt)
print(response)

print(f"words: {bcolors.OKGREEN}{len(response.split())}{bcolors.ENDC}")
