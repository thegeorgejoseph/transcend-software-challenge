import os
from urllib import request
import requests
import json
from dotenv import load_dotenv
from validate import *
import time 
import logging 
import http.client
import datetime 
load_dotenv()

# the api key
MAILGUN_API_KEY = os.environ.get("API_KEY")
#the base url
BASE_URL = os.environ.get("BASE_URL")
#cache
cache = {}

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

def getMailingLists(identifier,currentTime = None):
        mailing_lists =[]
        try:  
            start = time.time()
            res = requests.get(BASE_URL+"lists",auth=('api',MAILGUN_API_KEY))
            res.raise_for_status()
        except requests.exceptions.HTTPError as err:
           with open("errors.log","a") as log:
                log.write(f"{err} - {datetime.datetime.now()} ")
                log.write("\n") 
        except requests.exceptions.Timeout as err:
        #We could implement a Retry logic here but for now we will throw an error
            with open("errors.log","a") as log:
                log.write(f"{err} - {datetime.datetime.now()} ")
                log.write("\n") 
        except requests.exceptions.TooManyRedirects as err:
            with open("errors.log","a") as log:
                log.write(f"{err} - {datetime.datetime.now()} ")
                log.write("\n") 
        response_data = res.json()
        if response_data['total_count'] >= 1:
            for list_item in response_data['items']:
                if list_item['members_count'] > 0:
                    # mailing_lists.append(list_item['address'])
                    cache[list_item['address']] = []
        cache['last_updated_time'] = time.time() if currentTime is None else currentTime
        return 
    
def getMailingMembersForLists(identifier,currentTime = None):    
    for key,value in cache.items():
        if key == "last_updated_time":
            continue
        try:
            res = requests.get(BASE_URL+f"lists/{key}/members",auth=('api',MAILGUN_API_KEY))
            res.raise_for_status()
        except requests.exceptions.HTTPError as err:
            with open("errors.log","a") as log:
                log.write(f"{err} - {datetime.datetime.now()} ")
                log.write("\n")
        except requests.exceptions.Timeout as err:
        #We could implement a Retry logic here but for now we will throw an error
            with open("errors.log","a") as log:
                log.write(f"{err} - {datetime.datetime.now()} ")
                log.write("\n") 
        except requests.exceptions.TooManyRedirects as err:
            with open("errors.log","a") as log:
                log.write(f"{err} - {datetime.datetime.now()} ")
                log.write("\n") 
        result = []
        response_data = res.json()
        if "error" in response_data:
            continue
        with open('personal.json', 'w') as json_file:
                json.dump(response_data, json_file)
        for member in response_data['items']:
            result.append(member['address'])

        cache[key] = result 
    cache['last_updated_time'] = time.time() if currentTime is None else currentTime
    return

def getMatchingMailingList(identifier):
    result = []
    for key,values in cache.items():
        if key == "last_updated_time":
            continue
        with open("cache.json","w") as file:
            json.dump(cache,file)
        for value in values:
            # print(f"attemping {value}")
            if value == identifier:
                result.append(key)
                break
    return result

def accessHelper(identifier):
    # if validateEmail(identifier):
    #         response_data = getListOfDomains(identifier)
    # else:
    #     raise ValueError(f"Invalid Email Found {identifier}")

    # domain_lists = []
    
    # if response_data['total_count'] >0:
    #     for domain_item in response_data['items']:
    #         domain_lists.append(domain_item['name'])
            
    # if len(domain_lists) == 0:
    #     raise Exception("There are no domains related to this account") 
    
    #for the first time this is run we need to cache all the mailing lists
    if len(cache) == 0:
        getMailingLists(identifier)
        getMailingMembersForLists(identifier)
        
    if len(cache) == 0:
        raise Exception("There are no mailing lists associated with this account")
    
    if abs(cache['last_updated_time'] - time.time()) >= 86400: #making the api call once every 24 hours to have an updated mailing list
        getMailingLists(identifier,time.time())
        getMailingMembersForLists(identifier,time.time())   
    
    
    return getMatchingMailingList(identifier)
# get all the mailing lists the user belongs to
def access(identifier):
        data = accessHelper(identifier)    
        return {"data":data}
        


# remove the user from all mailing lists
def erasure(identifier, context):
    raise NotImplementedError('Erasure not implemented!')
