from data_util import csv2prompt_data

from watsonx import Watsonx

# use ibm cloud api key
# the one provided here is generated for our team
model = Watsonx('oQa6gs97JebPhsMvwaIKVsg6hHYcD7N5XxDXrbVd4-T9').model_ai('google/flan-ul2')
# use https://bam.res.ibm.com/ api key
# model = Watsonx('APIKEY').model_alpha('ibm/mpt-7b-instruct')

def prompt(input):
    print(model.prompt(input))

optical_density_txt_data = csv2prompt_data('TB_demo_v2.csv', column_list=['optical density'], max_rows=10)
monitor_photo_txt_data = csv2prompt_data('TB_demo_v2.csv', column_list=['Monitor photo density'], max_rows=10)

useful_column_list = [
    "BatchID", "Fidx", "elapsed time", "optical density", "Monitor photo density", "sheet resistance",
    "Hall resistance", "Hall resistivity", "conductivity", "Hall coefficient",
    "sigma square hall coefficient",
    "Hall density"
]

data = csv2prompt_data("TB_demo_v2.csv", column_list=useful_column_list, max_rows=0, lowercase_column_headers=False)
examples = ''
question = "Write a pandas dataframe query for finding the \"sigma square hall coefficient\" value when \"conductivity\" is 0.005789713"
answer = ''

template = f'''
Answer the following question using only information from the table. If there is no good answer in the article, say 'I don't know'.

Table:
###
{data}
###

{examples}

Q: {question}
A: {answer}
'''

print("--------Prompt--------")
print(template)
print("--------Answer--------")
prompt(template)
print("----------------------")

# prompt('the correlation between ' + optical_density_txt_data + ' and ' + monitor_photo_txt_data)
# prompt('the optimal density: ' + optical_density_txt_data + ' what is the maxinum of the optical density ')