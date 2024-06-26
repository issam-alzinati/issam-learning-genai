from utilities import *

final_response_to_customer = f"""
The SmartX ProPhone has a 6.1-inch display, 128GB storage,
12MP dual camera, and 5G. The FotoSnap DSLR Camera
has a 24.2MP sensor, 1080p video, 3-inch LCD, and
interchangeable lenses. We have a variety of TVs, including
the CineView 4K TV with a 55-inch display, 4K resolution,
HDR, and smart TV features. We also have the SoundMax
Home Theater system with 5.1 channel, 1000W output, wireless
subwoofer, and Bluetooth. Do you have any specific questions
about these products or any other products we offer?
"""
response = client.moderations.create(
    input=final_response_to_customer
)
moderation_output = response.results[0]
print(moderation_output)
