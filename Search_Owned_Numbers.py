############################################################
##### Title: Search Owned  Numbers                                                  #####
##### Author: Olivier Salmon                                                             #####
##### Date: 09 May 2018                                                                   #####
##### Updated:                                                                                   #####
##### Compatibility: Python 3                                                            #####
############################################################

import requests
import sys
import math
import os
import time
from requests_toolbelt.utils import dump

############
# SETTINGS #
############

### API KEY ###
params_keys = {
    'api_key': os.getenv('nexmo_api_key'),
    'api_secret': os.getenv('nexmo_api_secret')
}

### GLOBAL PARAMETERS ###
page_size = 10        # default 10, max 100
pattern = ''                 # A matching pattern (not required)
search_pattern = ''     # Strategy for matching pattern. Expected values: 0 (starts with, default), 1 (anywhere), 2 (ends with). (not required)

params_global = {
    'pattern': pattern,
    'search_pattern': search_pattern
}

numberList = []

###########
# CODE     #
###########


def roundup(x):
    return int(math.ceil(x))


def countOwnedNumbers():
    params = dict(params_keys.items())
    try:
        response = requests.get(base_url + action_search, params=params)
        virtual_numbers = response.json()
        return virtual_numbers['count']

    except requests.exceptions.RequestException as e:
        print(e)
        sys.exit(1)


def listOwnedNumbers(maxPageSize, idx):
    new_params = {
        'size': maxPageSize,
        'index': idx
    }

    params = dict(params_keys.items() | new_params.items() | params_global.items())

    try:
        response = requests.get(base_url + action_search, params=params)
        #data = dump.dump_all(response)
        #print(data.decode('utf-8'))
        virtual_numbers = response.json()
        for number in virtual_numbers['numbers']:
            print(number)

    except requests.exceptions.RequestException as e:
        print(e)
        sys.exit(1)


base_url = 'https://rest.nexmo.com'
version = ''
action_search = '/account/numbers'

ownedNumbers = countOwnedNumbers()
pagination = roundup(ownedNumbers / page_size)

# Need to wait a second - 1 request per second with the developer API
time.sleep(1)

if (pagination == 1):
    listOwnedNumbers(page_size, 1)
else:
    for x in range(1, pagination + 1):
        # Need to wait a second - 1 request per second with the developer API
        print("Page {} - {} numbers per page".format(x,page_size))
        time.sleep(1)
        listOwnedNumbers(page_size, x)
