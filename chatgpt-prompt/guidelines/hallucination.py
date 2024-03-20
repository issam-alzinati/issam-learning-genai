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


prompt3 = f"""
Tell me about AeroGlide UltraSlim Smart Toothbrush by Alzinati company.
highlight the resources you used, the steps you take to produce the content. If you dont feel condfident, say that you dont have enough context/info.
"""
response3 = get_completion(prompt3)
print(f"{bcolors.OKGREEN}{response3}{bcolors.ENDC}")