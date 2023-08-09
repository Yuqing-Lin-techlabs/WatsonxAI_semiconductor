import os
import pandas as pd

from Task1 import DATA_DIR, PROMPTS_DIR
from Task1 import csv2prompt_data, read_column_description
from langchain import PromptTemplate, LLMChain
from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames
from LLMService import llm

TASK1A_PROMPT = PromptTemplate.from_file(PROMPTS_DIR / "task1a_prompt.txt", ["data", "demonstrations",
                                                                             "question", "answer"])
all_column_list = ["BatchID", "Fidx", "elapsed time", "optical density", "Monitor photo density", "stage temperature",
                   "sample temperature", "monitor temperature", "Type", "Rxx State", "Rxy State", "sheet resistance",
                   "Hall resistance", "Hall resistivity", "conductivity", "Hall coefficient",
                   "sigma square hall coefficient",
                   "Hall density", "Hall mobility", "wavelength"
                   ]
CLN_D = read_column_description()


useful_column_list = ["BatchID", "Fidx", "elapsed time", "optical density", "Monitor photo density", "sheet resistance",
                      "Hall resistance", "Hall resistivity", "conductivity", "Hall coefficient",
                      "sigma square hall coefficient",
                      "Hall density"]
data= csv2prompt_data("TB_demo_v2.csv", column_list=useful_column_list, max_rows=10)
df = pd.read_csv(os.path.join(DATA_DIR,"TB_demo_v2.csv"))
model = llm(model_id=ModelTypes.FLAN_UL2)

demonstrations = ""
# demonstrations = """
# Q: What is the "sigma square hall coefficient" value when "conductivity" is 0.005789713?
# A: 0.000112568
#
# Q: What is the "conductivity" when "Fidx" is 4?
# A: 0.005780041
# """
question = "Write a pandas dataframe query for finding the \"sigma square hall coefficient\" value when \"conductivity\" is 0.005789713"
# question = "What is the elapsed time when Fidx is 3?" #739085.5217
# question = "What is the sigma square hall coefficient when Fidx is 3?" #0.000112127
# question = "What is the maximum of conductivity?" #0.006048771

prompt_txt = TASK1A_PROMPT.format(data=data, demonstrations=demonstrations, question=question, answer="")
print("\nprompt_txt")
print(prompt_txt)
gen_parms_override = {"MAX_NEW_TOKENS": 200}

generated_response = model.generate(prompt_txt, gen_parms_override)

# print(GenTextParamsMetaNames().show())
print("\nresult")
print(generated_response["results"][0]["generated_text"].strip())
print(eval(generated_response["results"][0]["generated_text"].strip()))
