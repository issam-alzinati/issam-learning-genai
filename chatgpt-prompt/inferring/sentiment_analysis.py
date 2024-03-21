from utilities import *
from product_reviews import *

prompt = f"""
What is the sentiment of the following product review, 
which is delimited with triple backticks?

Review text: '''{lamp_review}'''
"""
response = get_completion(prompt)
print(response)


prompt2 = f"""
What is the sentiment of the following product review, 
which is delimited with triple backticks?

Give your answer as a single word, either "positive"
or "negative".

Review text: '''{lamp_review}'''
"""
response2 = get_completion(prompt2)
print(f"Sentiment is {response2}")