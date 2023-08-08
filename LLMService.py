
import os
from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes
from ibm_watson_machine_learning.foundation_models import Model
import json


IBM_CLOUD_API_KEY = os.getenv("IBM_CLOUD_API_KEY")
PROJECT_ID = "0beb9015-cd6d-467e-84a6-99f07254c022"


my_credentials = {
    "url": "https://us-south.ml.cloud.ibm.com",
    "apikey": IBM_CLOUD_API_KEY

}


def llm(
    model_id = ModelTypes.MPT_7B_INSTRUCT2,
    gen_parms = None,
    space_id = None,
    verify = False
):
    return Model(model_id, my_credentials, gen_parms, PROJECT_ID, space_id, verify )
