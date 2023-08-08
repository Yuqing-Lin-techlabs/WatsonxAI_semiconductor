# WatsonxAI_semiconductor


## Task 1: Generate data-grounded insights

### Task 1a: Analyze LLM understanding in answering statistical questions from data

The task here is given the input data model should be able to answer several statistical questions such as LLM should be able to answer what is min/max/avg…. number in a column. 

- Input Prompt:
  - Data 
  - Demonstration 
    - Q1:
    - A1:
    - Q2:
    - A2:
  - QN: User input 

### Task 1b: LLM to understand the more complex phenomenon


- Input Prompt:
  - Data 
  - Phenomenon definition
  - Demonstration 
    - Q1:
    - A1:
    - Q2:
    - A2:
  - QN: User input 


### Requirements


- Since we are limited by the number of tokens in the prompt, we need to find better ways to fit the data files into the prompt concisely.
- Let’s fix to 2-3 phenomenon for now. 
- @Yueheng you decide what definitions you think are less complex and fix those definitions for now
- We need phenomenon definitions [@Yueheng]
- We need data and phenomenon output for that data  [@Yueheng]
- Specify what columns are important for what phenomenon.  [@Yueheng]

## Task 2: Plot Generation 
plot generation

---

## Setup
- `conda create -n watsonx python==3.10`
- `conda activate watsonx`
- `pip install ibm-watson-machine-learning`
- Our project key is common, so I left it as it is in the code
  - You can find it here https://dataplatform.cloud.ibm.com/projects/0beb9015-cd6d-467e-84a6-99f07254c022/manage/general?context=wx
- you also need IBM cloud key which is personal.
  - First create your CLOUD API key https://cloud.ibm.com/iam/apikeys
  - and save it to your bash as `export IBM_CLOUD_API_KEY=<key>`

