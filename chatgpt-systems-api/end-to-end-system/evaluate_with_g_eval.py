from utilities import *
from all_products import *
from process_products import *

# Evaluation prompt template based on G-Eval
EVALUATION_PROMPT_TEMPLATE = """
You will be given an answer written for a question about product or collection or products. 
Your task is to rate the summary on one metric.
Please make sure you read and understand these instructions very carefully. 
Please keep this document open while reviewing, and refer to it as needed.

Evaluation Criteria:

{criteria}

Evaluation Steps:

{steps}

Example:

Related Products:

{related_products}

Answer:

{answer}

Evaluation Form (scores ONLY):

- {metric_name}
"""

# Metric 1: Relevance

RELEVANCY_SCORE_CRITERIA = """
Relevance(1-5) - selection of important content from the source. \
The answer should include only important information from the related products. \
Annotators were instructed to penalize answers which contained redundancies and excess information.
"""

RELEVANCY_SCORE_STEPS = """
1. Read the answer and the source document carefully.
2. Compare the answer to the source document and identify the main points of the question.
3. Assess how well the answer covers the main points of the question, and how much irrelevant or redundant information it contains.
4. Assign a relevance score from 1 to 5.
"""

# Metric 2: Coherence

COHERENCE_SCORE_CRITERIA = """
Coherence(1-5) - the collective quality of all sentences. \
We align this dimension with the DUC quality question of structure and coherence \
whereby "the answer should be well-structured and well-organized. \
The answer should not just be a heap of related information, but should build from sentence to a\
coherent body of related products."
"""

COHERENCE_SCORE_STEPS = """
1. Read the related products carefully and identify the main topic and key points.
2. Read the answer and compare it to the article. Check if the answer covers the main topic and key points of the related products,
and if it presents them in a clear and logical order.
3. Assign a score for coherence on a scale of 1 to 5, where 1 is the lowest and 5 is the highest based on the Evaluation Criteria.
"""

# Metric 3: Consistency

CONSISTENCY_SCORE_CRITERIA = """
Consistency(1-5) - the factual alignment between the answer and the related products. \
A factually consistent answer contains only statements that are entailed by the related products. \
Annotators were also asked to penalize answers that contained hallucinated facts.
"""

CONSISTENCY_SCORE_STEPS = """
1. Read the related products carefully and identify the main facts and details it presents.
2. Read the answer and compare it to the related products. Check if the answer contains any factual errors that are not supported by the related products.
3. Assign a score for consistency based on the Evaluation Criteria.
"""

# Metric 4: Fluency

FLUENCY_SCORE_CRITERIA = """
Fluency(1-3) - the quality of the answer in terms of grammar, spelling, punctuation, word choice, and sentence structure.
1: Poor. The answer has many errors that make it hard to understand or sound unnatural.
2: Fair. The answer has some errors that affect the clarity or smoothness of the text, but the main points are still comprehensible.
3: Good. The answer has few or no errors and is easy to read and follow.
"""

FLUENCY_SCORE_STEPS = """
Read the answer and evaluate its fluency based on the given criteria. Assign a fluency score from 1 to 3.
"""


def get_geval_score(
    criteria: str, steps: str, related_products: str, answer: str, metric_name: str
):
    prompt = EVALUATION_PROMPT_TEMPLATE.format(
        criteria=criteria,
        steps=steps,
        metric_name=metric_name,
        related_products=related_products,
        answer=answer,
    )
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        max_tokens=5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    return response.choices[0].message.content


evaluation_metrics = {
    "Relevance": (RELEVANCY_SCORE_CRITERIA, RELEVANCY_SCORE_STEPS),
    "Coherence": (COHERENCE_SCORE_CRITERIA, COHERENCE_SCORE_STEPS),
    "Consistency": (CONSISTENCY_SCORE_CRITERIA, CONSISTENCY_SCORE_STEPS),
    "Fluency": (FLUENCY_SCORE_CRITERIA, FLUENCY_SCORE_STEPS),
}

customer_msg = f"""
tell me about the smartx pro phone and the fotosnap camera, the dslr one.
Also, what TVs or TV related products do you have?"""
# customer_msg = f"""What could be a good present for my videographer friend?"""
# customer_msg = f"""I need a charger for my smartphone"""

products_by_category = find_category_and_product_v3(customer_msg, get_products_and_category())
category_and_product_list = read_string_to_list(products_by_category)
product_info = generate_output_string(category_and_product_list)
assistant_answer = answer_user_msg(user_msg=customer_msg, product_info=product_info)

print(f'{bcolors.HEADER}{customer_msg}{bcolors.ENDC}')
print(f'{bcolors.OKCYAN}{assistant_answer}{bcolors.ENDC}')

for eval_type, (criteria, steps) in evaluation_metrics.items():
        result = get_geval_score(criteria, steps, product_info, assistant_answer, eval_type)
        score_num = float(result.strip())
        print(f'{bcolors.OKGREEN}{eval_type}: {score_num}{bcolors.ENDC}')
