from utilities import *

user_messages = [
  "La performance du système est plus lente que d'habitude.",               # System performance is slower than normal         
  "Mi monitor tiene píxeles que no se iluminan.",                           # My monitor has pixels that are not lighting
  "Il mio mouse non funziona",                                              # My mouse is not working
  "Mój klawisz Ctrl jest zepsuty",                                          # My keyboard has a broken control key
  "我的屏幕在闪烁",                                                           # My screen is flashing
  "لدي مشكلة في البريد الإلكتروني الخاص بي في Outlook، وأحتاج إلى حل سريع",  # I have problem with my outlook email, I need quick fix
] 

for issue in user_messages:
    prompt = f"Tell me what language this is: ```{issue}```"
    lang = get_completion(prompt)
    print(f"Original message ({lang}): {issue}")

    prompt = f"""
    Translate the following  text to English 
    and Korean: ```{issue}```
    """
    response = get_completion(prompt)
    print(response, "\n")
