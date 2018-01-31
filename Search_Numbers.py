############################################################
##### Title: Bulk Check Numbers                        #####
##### Author: Olivier Salmon                           #####
##### Date: 24 March 2017                              #####
##### Updated: 9 September 2017                        #####
##### Compatibility: Python 3                          #####
############################################################

import requests
import sys
import math
import os

############
# SETTINGS #
############

### API KEY ###
params_keys = {
    'api_key': os.getenv('nexmo_api_key'),
    'api_secret': os.getenv('nexmo_api_secret')
}

### GLOBAL PARAMETERS ###
numberOfWantedNumbers = 10
amountOfSequentialsNumbers = 0

params_global = {
    'country': 'GB',
    # Possible values for features: SMS - VOICE - VOICE,SMS
    'features': 'SMS'
}

numberList = []

###########
# CODE    #
###########

def roundup(x):
    # return int(math.ceil(x / 10.0)) * 10
    return int(math.ceil(x))

def getNumbers(maxPageSize,idx):
    new_params = {
        'size': maxPageSize,
        'index':idx
    }

    print(idx)

    params = dict(params_keys.items() | new_params.items() | params_global.items())

    try:
        response = requests.get(base_url + action, params=params)
        virtual_numbers = response.json()
        print(virtual_numbers)
        for number in virtual_numbers['numbers']:
            print(number)
            print(number['msisdn'])
            numberList.append(number['msisdn'])
            if len(numberList) > 1 and len(numberList) < amountOfSequentialsNumbers:
                beforeLastNum = int(numberList[-2])
                lastNum = int(number['msisdn'])
                seqNum = lastNum - beforeLastNum
                #print(idx," ",beforeLastNum, " " , lastNum, " " , seqNum )
                if seqNum != 1:
                    numberList.clear()
            if len(numberList) == amountOfSequentialsNumbers:
                print(numberList)
                print(len(numberList))
                break
            country = number['country']
            msisdn = number['msisdn']

    except requests.exceptions.RequestException as e:
        print(e)
        sys.exit(1)


bigLoop = roundup (numberOfWantedNumbers/100)
smallLoop = numberOfWantedNumbers - ((bigLoop - 1) * 100)
#print(bigLoop)
#print(smallLoop)

base_url = 'https://rest.nexmo.com'
version = ''
action = '/number/search?'

if ((bigLoop-1) == 0):
    getNumbers(smallLoop,1)
else:
    for x in range(1, bigLoop):
        getNumbers(100,x)
    getNumbers(smallLoop)
