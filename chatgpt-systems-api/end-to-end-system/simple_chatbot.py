from context_setup import *
from prompt_toolkit import prompt # https://opensource.com/article/17/5/4-practical-python-libraries

messages =  [  
{'role':'system', 'content':'You are Service Assistant.'},
]

while 1:
    user_input = prompt('>')
    if user_input == "bye":
        break
    messages.append({'role':'user','content':user_input})
    response,messages = process_user_message(user_input,messages)
    print(f'{bcolors.OKGREEN}{response}{bcolors.ENDC}')
    messages.append({'role':'assistant', 'content':response})
