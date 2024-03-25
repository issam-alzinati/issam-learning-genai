# ChatGPT Prompt Engineering for Developers
*Course link: [https://learn.deeplearning.ai/courses/chatgpt-prompt-eng](https://learn.deeplearning.ai/courses/chatgpt-prompt-eng)*


## Guidelines

**Prompting Principles**

* *Principle 1*: Write clear and specific instructions
    * [Tactic 1](./guidelines/p1_tactic_1.py): Use delimiters to clearly indicate distinct parts of the input

    * [Tactic 2](./guidelines/p1_tactic_2.py): Ask for a structured output -> Json or HTML Ex: Provide them in JSON format with the following keys:...

    * [Tactic 3](./guidelines/p1_tactic_3.py): Ask the model to check whether conditions are satisfied

    * [Tactic 4](./guidelines/p1_tactic_4.py): "Few-shot" prompting

* *Principle 2*: Give the model time to “think”
    * [Tactic 1](./guidelines/p2_tactic_1.py): Specify the steps required to complete a task
    * [Tactic 2](./guidelines/p2_tactic_2.py): Instruct the model to work out its own solution before rushing to a conclusion

**Model Limitations: Hallucinations**
LLM is able to produce a realistic text that sounds pretty good but [far from truth(hallucinations)](./guidelines/hallucination.py), so you need to double check any result. You can start by asking for resources, steps taken to generate the text and other tactics used before. [See prompt 3 in the code example on how to verify hallucinations](./guidelines/hallucination.py).


## Iterative
The idea is to keep iterating over the prompt till you get a satisfactory result for the task you are trying to do.

**Iterative Prompt Development**
1. Idea
2. Prompt(Writing/Implementation)
3. Experiment results & Error Analysis
    * Analyze why results don't give the desired output
    * Refine Idea and the Prompt
    * Repeat
4. Decide on the final output format

**Example:**
We have a product with a complete information. Here are the prompts sequence:
1. [Create description for marketing team](./iterative/first_run.py)
2. [Summarize the description to be shorter for the marketing team](./iterative/short_desc.py)
3. To get better result(correct the model), give more details about the marketing team target, like this [summary will target the furniture retails](./iterative/desc_intended_audience.py) then [add the product ID](./iterative/desc_audience_prod_id.py) to the end of the description
4. Extract more details needed in the summary. Ex: [add product dimension](./iterative/desc_product_dimension.py)
5. Format the output as [HTML page](./iterative/desc_product_dimension_html.py)


## Summarizing
1. Summarize based on limits, [characters, words, sentences](./summarizing/limits.py).
2. Summarize based on specific relevancy:
    * Specific to a department, like customer experience
    * Specific to a topic/data like price and value
3. Even when we specify the summary relevancy, the generated summary might include not related topics.
4. [Extraction](./summarizing/extract.py) could be another technique to use for finding relevant information.
5. [Finally it is powerful when it applies to summarize a collection of inputs/reviews](./summarizing/summarize_multiple_reviews.py).


## Inferring
Which is performing some analysis to extracting key data like labels, names, and understanding the sentiment of the text.
1. Do sentiment analysis, and specify output form(positive, negative)
2. [Identify type of emotions](./inferring/type_of_emotions.py), or specify if one emotion is exist, [ex: anger](./inferring/identify_anger.py).
3. Extract specific information, [like product and company name](./inferring/extract_names.py).
4. [Then you can combine all the above tasks as one!](./inferring/multiple_tasks.py)
5. [You can also infer topics in news and stories](./inferring/extract_topics.py)
6. [Or check if a list of topics are covered in a news article or a stroy](./inferring/verify_topics.py)


## Transforming
Models for text transformation tasks such as language translation, spelling and grammar checking, tone adjustment, and format conversion.

1. Translation
    * [Simple translation](./transforming/simple_translation.py)
    * [Detecting language](./transforming/detect_language.py)
    * [Multiple translation languages](./transforming/multiple_translation.py)
    * [Formal vs InFormal translation](./transforming/formal_informal_translation.py)
    * Imagine you are in charge of IT at a large multinational e-commerce company. Users are messaging you with IT issues in all their native languages. Your staff is from all over the world and speaks only their native languages. [You need a universal translator!](./transforming/universal_translator.py)
2. [Tone Transformation](./transforming/tone.py)
3. [Format Conversion](./transforming/format_conversion.py)
4. [Spellcheck/Grammar check](./transforming/spellcheck.py)


## Expanding
Expanding a text of an email or essay to be longer, this could be a case of using LLM as a brainstorming partner.

1. [Send reply email to customer review](./expanding/send_reply_email.py)
2. [Send reply email but use details from the customer review](./expanding/send_reply_emial_with_details.py)


## Chatbot

OpenAI chat model support 3 different types of roles per message when you leverage the model:
1. System Role: Gives overall instruction and guidelines for the chat model
2. Assistant Role: Is the agent the will keep communicating with the user based on the earlier instruction passed to the system
3. User Role: Is the user messages

![Chat Model Roles](./chatbot/img/chatmodel.png?raw=true)

Examples of using ChatGPT as a bot:
1. [Simple and Friendly chatbot](./chatbot/friendly_chatbot.py), nothing much on the context(System).
2. [Shakespeare chat bot](./chatbot/shakespeare.py), this is based on simple instructions passed to the context(System).
3. [Pizza order bot](./chatbot/orderbot.py), passing complex system instructions and have the changed during the chat lifecycle.
