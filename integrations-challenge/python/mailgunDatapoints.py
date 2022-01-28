import os
import requests
import json
from dotenv import load_dotenv
from validate import *

load_dotenv()

# the api key
MAILGUN_API_KEY = os.environ.get("API_KEY")
BASE_URL = os.environ.get("BASE_URL")

# create mailing lists and seed users into them
def seed(identifier):
    raise NotImplementedError('Seeding not implemented!')


# get all the mailing lists the user belongs to
def access(identifier):
    if validateEmail(identifier):
        try:
            res = requests.get(BASE_URL+"domains",auth=('api',MAILGUN_API_KEY))
        except requests.exceptions.Timeout:
            #We could implement a Retry logic here but for now we will throw an error
            raise Exception("Request Timed Out")
        except requests.exceptions.TooManyRedirects:
            raise Exception("Bad URL, Try Again")
        
        response_data = res.json()
        domain_list = []

        with open('personal.json', 'w') as json_file:
            json.dump(response_data, json_file)
            
        if response_data['total_count'] >0:
            for domain_item in response_data['items']:
                domain_list.append(domain_item['name'])
                
        if len(domain_list) == 0:
            raise Exception("There are no domains related to this account")
        
        
                
    else:
        raise ValueError(f"Invalid Email Found {identifier}")


# remove the user from all mailing lists
def erasure(identifier, context):
    raise NotImplementedError('Erasure not implemented!')
