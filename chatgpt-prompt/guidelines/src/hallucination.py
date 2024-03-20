from utilities import *

prompt = f"""
Tell me about AeroGlide UltraSlim Smart Toothbrush by Boie
"""
response = get_completion(prompt)
print(response)


prompt2 = f"""
Tell me about AeroGlide UltraSlim Smart Toothbrush by Alzinati company
"""
response2 = get_completion(prompt2)
print(f"{bcolors.HEADER}{response2}{bcolors.ENDC}")