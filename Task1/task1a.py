from Task1 import DATA_DIR, PROMPTS_DIR
from Task1 import csv2prompt_data, read_column_description
from langchain import PromptTemplate, LLMChain
from LLMService import llm

TASK1A_PROMPT = PromptTemplate.from_file(PROMPTS_DIR / "task1a_prompt.txt", ["data", "demonstrations",
                                                                             "question", "answer"])
all_column_list = ["BatchID", "Fidx", "elapsed time", "optical density", "Monitor photo density", "stage temperature",
                   "sample temperature", "monitor temperature", "Type", "Rxx State", "Rxy State", "sheet resistance",
                   "Hall resistance", "Hall resistivity", "conductivity", "Hall coefficient",
                   "sigma square hall coefficient",
                   "Hall density", "Hall mobility", "wavelength"
                   ]
CLN_D= read_column_description()





question = "What is the elapsed time when Fidx is 3?"
useful_column_list = ["BatchID", "Fidx", "elapsed time", "optical density", "Monitor photo density", "sheet resistance",
                      "Hall resistance", "Hall resistivity", "conductivity", "Hall coefficient",
                      "sigma square hall coefficient",
                      "Hall density"]
data = csv2prompt_data("TB_demo_v2.csv", column_list=useful_column_list, max_rows=10)
model = llm()
prompt_txt = TASK1A_PROMPT.format(data=data, demonstrations="", question=question, answer="")
print(prompt_txt)
gen_parms_override = None

generated_response = model.generate(prompt_txt, gen_parms_override)
print(generated_response["results"])