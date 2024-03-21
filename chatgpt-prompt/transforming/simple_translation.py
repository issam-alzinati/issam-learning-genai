from utilities import *

prompt = f"""
Translate the following English text to Spanish: 
```Hi, I would like to order a blender```
"""
response = get_completion(prompt)
print(response)
