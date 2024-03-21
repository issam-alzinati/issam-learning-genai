from utilities import *
from product_reviews import *

topic_list = [
    "nasa", "local government", "engineering", 
    "employee satisfaction", "federal government"
]

prompt = f"""
Determine whether each item in the following list of
topics is a topic in the text below, which
is delimited with triple backticks.

Give your answer as list with 0 or 1 for each topic.

List of topics: {", ".join(topic_list)}

Text sample: '''{story}'''
"""
response = get_completion(prompt)
print(response)

topic_mask = response.split('\n')[0][1:-1].split(sep=', ')
if topic_mask[0] == '1':
    print("ALERT: New NASA story!")
