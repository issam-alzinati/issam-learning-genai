from utilities import *
from review import *

prompt = f"""
You are a customer service AI assistant.
Your task is to send an email reply to a valued customer.
Given the customer email delimited by ```,
Generate a reply to thank the customer for their review.
If the sentiment is positive or neutral, thank them for
their review.
If the sentiment is negative, apologize and suggest that
they can reach out to customer service. 
Make sure to use specific details from the review.
Write in a concise and professional tone.
Sign the email as `AI customer agent`.
Customer review: ```{review}```
Review sentiment: {sentiment}
"""
response = get_completion(prompt, temperature=0.7)
print(response)
