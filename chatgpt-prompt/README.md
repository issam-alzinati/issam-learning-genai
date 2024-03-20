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

