from utilities import *

prompt = f"""
Translate the following text to Spanish in both the
formal and informal forms: 
'Would you like to order a pillow?'
"""
response = get_completion(prompt)
print(response)