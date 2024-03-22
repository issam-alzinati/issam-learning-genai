from utilities import *
from prompt_toolkit import prompt # https://opensource.com/article/17/5/4-practical-python-libraries

messages =  [  
{'role':'system', 'content':'You are friendly chatbot.'},
]

while 1:
    user_input = prompt('>')
    if user_input == "bye":
        break
    messages.append({'role':'user','content':user_input})
    response = get_completion_from_messages(messages, temperature=1)
    print(response)
