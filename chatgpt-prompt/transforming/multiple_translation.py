from utilities import *

prompt = f"""
Translate the following  text to French and Spanish
and English pirate:
```I want to order a basketball```
"""
response = get_completion(prompt)
print(response)
