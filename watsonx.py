import requests

class Watsonx:
    def __init__(self, api_key):
        self.api_key = api_key

    def model_ai(self, model_id):
        return Model_ai(self.api_key, model_id)
    
    def model_alpha(self, model_id):
        return Model_alpha(self.api_key, model_id)

class Model_ai:
    def __init__(self, api_key, model_id):
        self.api_key = api_key
        self.model_id = model_id

    def prompt(self, input):
        auth_resp = requests.post(
            'https://iam.cloud.ibm.com/identity/token',
            data={
                'apikey': self.api_key,
                'grant_type': 'urn:ibm:params:oauth:grant-type:apikey'
            }
        )
        access_token = auth_resp.json()['access_token']

        payload = { 
            'model_id': self.model_id,
            'input': input,
            'parameters': {
                'decoding_method': 'greedy',
                'max_new_tokens': 20,
                'min_new_tokens': 0,
                'stop_sequences': [],
                'repetition_penalty': 1
            },
            'project_id': '0beb9015-cd6d-467e-84a6-99f07254c022'
        }

        prompt_resp = requests.post(
            'https://us-south.ml.cloud.ibm.com/ml/v1-beta/generation/text?version=2023-05-29',
            headers={
                'Authorization': 'Bearer ' + access_token
            },
            json=payload
        )

        return prompt_resp.json()['results'][0]['generated_text']
    
class Model_alpha:
    def __init__(self, api_key, model_id):
        self.api_key = api_key
        self.model_id = model_id

    def prompt(self, input):
        payload = { 
            'model_id': self.model_id,
            'inputs': [input],
            'parameters': {
                'decoding_method': 'greedy',
                'max_new_tokens': 200,
                'min_new_tokens': 1,
                'repetition_penalty': 1
            }
        }

        prompt_resp = requests.post(
            'https://bam-api.res.ibm.com/v1/generate',
            headers={
                'Authorization': 'Bearer ' + self.api_key,
                'Content-Type': 'application/json'
            },
            json=payload
        )

        return prompt_resp.json()['results'][0]['generated_text']