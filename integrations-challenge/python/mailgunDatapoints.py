import os
from urllib import request
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


def getListOfDomains(identifier):
    try:
        res = requests.get(BASE_URL+"domains",auth=('api',MAILGUN_API_KEY))
    except requests.exceptions.Timeout:
        #We could implement a Retry logic here but for now we will throw an error
        raise Exception("Request Timed Out")
    except requests.exceptions.TooManyRedirects:
        raise Exception("Bad URL, Try Again")
    
    return res.json()

def getMailingLists(identifier):
        mailing_lists =[]
        try:  
            res = requests.get(BASE_URL+"lists",auth=('api',MAILGUN_API_KEY))
            response_data = res.json()
            if response_data['total_count'] >= 1:
                for list_item in response_data['items']:
                    if list_item['members_count'] > 0:
                        mailing_lists.append(list_item['address'])
        except requests.exceptions.Timeout:
        #We could implement a Retry logic here but for now we will throw an error
            raise Exception("Request Timed Out")
        except requests.exceptions.TooManyRedirects:
            raise Exception("Bad URL, Try Again")
        return mailing_lists
# get all the mailing lists the user belongs to
def access(identifier):
    
        if validateEmail(identifier):
            response_data = getListOfDomains(identifier)
        else:
            raise ValueError(f"Invalid Email Found {identifier}")

        domain_lists = []
        result = []
        
        if response_data['total_count'] >0:
            for domain_item in response_data['items']:
                domain_lists.append(domain_item['name'])
                
        if len(domain_lists) == 0:
            raise Exception("There are no domains related to this account") 
        
        
        mailing_lists = getMailingLists(identifier)
        
        if len(mailing_lists) == 0:
            raise Exception("There are no mailing list associated with this account")
        
        for list_item in mailing_lists:
            print(f"Attemping {list_item} mailing list")
            try:
                res = requests.get(BASE_URL+f"lists/{list_item}/members",auth=('api',MAILGUN_API_KEY))
                response_data = res.json()
        
                # with open('personal.json', 'w') as json_file:
                #         json.dump(response_data, json_file)
                for member in response_data['items']:
                    if member['address'] == identifier:
                        result.append(list_item)
                        # print(f"Added Mailing List {list_item}")
                        break
            except:
                pass
        return {"data":result}
        


# remove the user from all mailing lists
def erasure(identifier, context):
    raise NotImplementedError('Erasure not implemented!')
