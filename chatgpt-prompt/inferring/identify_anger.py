from utilities import *
from product_reviews import *

prompt = f"""
Is the writer of the following review expressing anger?
The review is delimited with triple backticks.
Give your answer as either yes or no.

Review text: '''{lamp_review}'''
"""
response = get_completion(prompt)
print(response)

