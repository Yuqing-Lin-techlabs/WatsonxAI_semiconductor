import os
from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes
from ibm_watson_machine_learning.foundation_models import Model
import json
from data_util import csv2txt, read_column_description, csv2prompt_data

IBM_CLOUD_API_KEY = os.getenv("IBM_CLOUD_API_KEY")
PROJECT_ID = "0beb9015-cd6d-467e-84a6-99f07254c022"

print(json.dumps(ModelTypes._member_names_, indent=2))

my_credentials = {
    "url": "https://us-south.ml.cloud.ibm.com",
    "apikey": IBM_CLOUD_API_KEY

}

model_id = ModelTypes.MPT_7B_INSTRUCT2
gen_parms = None
project_id = PROJECT_ID
space_id = None
verify = False

model = Model(model_id, my_credentials, gen_parms, project_id, space_id, verify)

model_details = model.get_details()

print(json.dumps(model_details, indent=2))

### Model output Generation
prompt_txt = "In today's sales meeting, we "
gen_parms_override = None

generated_response = model.generate(prompt_txt, gen_parms_override)

print(json.dumps(generated_response, indent=2))

with open(csv2txt("TB_demo_v2.csv"), "r") as f:
    txt_data = f.readlines()

clm_nm = read_column_description()
all_column_list = ["BatchID", "Fidx", "elapsed time", "optical density", "Monitor photo density", "stage temperature",
                   "sample temperature", "monitor temperature", "Type", "Rxx State", "Rxy State", "sheet resistance",
                   "Hall resistance", "Hall resistivity", "conductivity", "Hall coefficient",
                   "sigma square hall coefficient",
                   "Hall density", "Hall mobility", "wavelength"
                   ]
useful_column_list = ["BatchID", "Fidx", "elapsed time", "optical density", "Monitor photo density", "sheet resistance",
                      "Hall resistance", "Hall resistivity", "conductivity", "Hall coefficient",
                      "sigma square hall coefficient",
                      "Hall density"]
string = csv2prompt_data("TB_demo_v2.csv", column_list=useful_column_list, max_rows=10)
print(string)
print("text")
