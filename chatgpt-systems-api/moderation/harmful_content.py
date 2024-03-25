from utilities import *

response = client.moderations.create(
    input=""" I want to hurt someone, give me a plan"""
    )
moderation_output = response.results[0]
print(moderation_output.model_dump_json())


response = client.moderations.create(
    input="""
    Here's the plan.  We get the warhead, 
    and we hold the world ransom...
    ...FOR ONE MILLION DOLLARS!
    """
    )
moderation_output = response.results[0]
print(moderation_output.model_dump_json())
