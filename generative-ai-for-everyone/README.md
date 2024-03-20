# Generative AI for Everyone
*course link: [https://www.coursera.org/learn/generative-ai-for-everyone](https://www.coursera.org/learn/generative-ai-for-everyone)*


## GenAI
The power of GenAI is to help you do your job efficiently and this is the leaders job to convince the teams of that and help them upskilling. GenAI can also be a reasoning engine and a thought partner after being fed with the write data.

GenAI is built on top of LLM that used a lot of power and data using hundreds of millions on input parameters

GenAI has many applications: Routing mails, summarizing, direction, analyzing of sentiment, etc...

GenAI can be thought as thought partner for brain storming

GenAI usage can be extracted based on 3 types of usage:
1. Writing
2. Reading
3. Chatting
Based on that we can use web interfaces or applications that are built on top of LLMs or custom LLMs

Applying LLM:
1. Reading
* Routing
* Reputation monitoring
* Summarizing, ex: call center
* Proofreading
2. Writing
* Brain storming
* Planing
* Emails, official communications, press releases
* Translation
3. Chatting
* Build chatbot into phases:
    * Internal facing
    * Human in loop
    * Communicate directly with customers but no complete
    * Take over

What LLM cannot do:
1. Knowledge cutoff: Trained on specific period of time
2. Limited to context you provide, imagine fresh graduate
3. Make things up, hallucinations
4. Limited length of input and output
5. Doesn't work well with tabular data
6. Biased - Example gender bias


Be carful with:
1. Confidential data
2. Verify the content


## GenAI prompt

What is needed to get high quality output, is to provide structured prompt that includes with order of importance:
1. Task
2. Context
3. examplar
4. persona
5. format
6. tone

In general:
1. Be detailed and specific
2. Guid the model to think through the answer
3. Experiment and Iterate: Idea->Prompt->LLM Response

## GenAI software development

Software applications based on **LLM** has the following **development lifecycle**:

scope -> build/develop -> internal assessment -> customer monitoring

**LLM Cost**:
It based on input and output tokens. Each token is 3/4 of a word <-> a word is 1.33 token

**LLM** have a lot of knowledge but dont know everything, then it should be considers as a **reasoning engine** to process information not as a source of information

Development techniques to build LLM software applications beyond prompt:
1. **Retrieval Augmented Generation(RAG) - Modification of Prompt - cheap**: Is a way to give answer based on a context that being pulled at the time the question being asked.
* Give a question, search relevant documents for the answer
* Incorporated retrieved text into an updated prompt
* Generate the answer from the new prompt with additional context(this can also provide reference to original document like lilli does)
2. **Fine-Tuning - Provide small number of inputs - cheap**: provide special knowledge to the model to tweek its results
* To carry out a task that is not easy to define in a prompt.
    * Summarize in a certain style or structure... like summarize support call with specific information about the product model, issue, customer no, etc...
    * mimicking a writing or speaking style. Like write a novel like Shakespeare. OR read in the voice of someone.
* Help LLM gain specific knowledge
    * Summarize legal documents, medical notes, or finance documents
* To get a smaller model to perform a specialized task -> this lower the running cost and response latency + enable to run the model on edge devices(Mobile, IoT, Laptops)
    * Create reputation monitoring for a restaurant.
3. **Retraining an LLM - Learning Big Specialized knowledge - Expensive**: pretrain general purpose LLM by learning from huge specific knowledge source
* It may take 10s of millions, many months, and huge a mount of data
* Last resorts
* Help specialized organization with huge source of knowledge like Bloomberg. They built a 50B parameter LLM from scratch to be purpose built for finance


### How to choose a model?

**Model Size**
| Size           | Power                                                  | Application                 | Enhancement |
|----------------|--------------------------------------------------------|-----------------------------|-------------|
| 1B Parameter   | pattern matchining and basic knowledge of the world    | Restaurant sentiment review | ARG         |
| 10B Parameter  | Greater world knoweldge. Can follow basic instructions | Chatbots                    | Fine-Tune   |
| 100B Parameter | Rich world knowledge. Complex reasoning                | Brainstorimng partner       | Fine-Tune   |


**Closed or Open Sourced**
| **Closed Source**                                                                   | **Open Source**                                                                                                                                |
|-------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| * Easy to use in applications * More large/powerful models * Relatively inexpensive | * full control over the model(Verify content and tune the model) * Can run on your own infra * Full control over data, privecy, and compliance |
| * some risk of vendor lock-in * Data privacy * compliance                           | * Expensive * Hard to develop and deploy                                                                                                       |
| * Any application can be built on top of closed sources                             | * Special health records analysis, where patient records can not be uploaded to cloud                                                          |

### How to train LLM:
Pretrains on fine tuned answers
Use **RLHF** (Reinforcement learning from human feedback. **Honest, helpful, and Harmless 3H**):
* Train an answer quality(reward) model. You can use multiple answers with scores
* Have LLM to generate a lot answers. Further train it to generate more responses that et high scores


## GenAI & Business

### Business cases
1. Use web UI to access GenAI and use it for day to day work
    * writing assistance
    * Summarize
    * Rewrite for different tunes
    * Proofreading
    * Brainstorm to create market materials and email campaigns
    * Recruiters to summarize reviews and get sentiments
    * Analyse sentiment of feedback
    * Programers can write code
    * Thought partners
2. Systematic framework to:
    * analyse the business and identify opportunities to use GenAI
        * You can analyse certain job tasks by listing all the tasks using https://www.onetonline.org/ or similar sites https://www.similarweb.com/website/onetonline.org/competitors/
        * Every job has appealing task that is associated to it and everyone one wants to automate. This might be difficult to achieve. It is better to check all the other tasks that is done by a job role, example:
            * Computer programmers do coding. Coding could be hard to do using GenAI. But think of other tasks like writing documentation and answering support questions. The later two tasks can be done using GenAI in easier way than coding!
    * augment and automate different tasks(Not jobs),
        * Augmentation: Help human to do a task... like recommend a response
        * Automation: Automatically perform and complete a task... like automatically summarize the customer interactions
    * Evaluating AI potential
        * Technical feasibility
            * Can AI do it? Cann prompt do that?
            * How much it cost to do that
            * Can application techniques be used, like RAG and fine-tune?
        * Business value
            * How valuable is it to augment/automate is task? How much time spent on this task? This analysis can be done for either employees or customer.
                * Employee: use GenAI to help developers write code, testing, and documentation
                * Customer: A customer that create website from template might use GenAI to generate the SEO content, website content, write a title
            * Does doing this task significantly faster, cheaper, or more consistently create a substantial value?
            * It is not only about cost saving! We should also the seek for growth opportunities as cost saving has a limit but growth does not. So always check how GenAI can help in growth.
                *  Example: When a task is discussed for automation it is good to rethink of a workflow of how the business create value. Instead of answering customer requests and build a system to do that answer. Automate the request as a feature itself.
                * Lawyer & Marketer examples

![alt text](img/legal_doc_review.png?raw=true)
![alt text](img/marketing_automation.png?raw=true)

3. Identify building or buying LLM based software applications can add value
