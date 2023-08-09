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

# prompt('the correlation between ' + optical_density_txt_data + ' and ' + monitor_photo_txt_data)
prompt('the optimal density: ' + optical_density_txt_data + ' what is the maxinum of the optical density ')
