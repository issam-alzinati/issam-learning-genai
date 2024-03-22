from utilities import *
from prompt_toolkit import prompt # https://opensource.com/article/17/5/4-practical-python-libraries

messages =  [  
{'role':'system', 'content':'You are an assistant that speaks like Shakespeare.'},    
{'role':'user', 'content':'tell me a joke'},   
{'role':'assistant', 'content':'Why did the chicken cross the road'},   
{'role':'user', 'content':'I don\'t know'}  ]

response = get_completion_from_messages(messages, temperature=1)
print(response)

while 1:
    user_input = prompt('>')
    if user_input == "exit":
        break
    messages.append({'role':'user','content':user_input})
    response = get_completion_from_messages(messages, temperature=1)
    print(response)

