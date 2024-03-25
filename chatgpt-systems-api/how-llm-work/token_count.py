from utilities import *

messages = [
{'role':'system', 
 'content':"""You are an assistant who responds
 in the style of Dr Seuss."""},    
{'role':'user',
 'content':"""write me a very short poem
 about a happy carrot"""},  
] 
response, token_dict = get_completion_and_token_count(messages)

print(response)

print(token_dict)
