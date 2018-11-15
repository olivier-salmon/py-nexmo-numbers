# Searching and renting Nexmo's numbers
Use the Nexmo's API to check phone numbers availability or rent them 

# Pre-requisites

* open a Nexmo account
* make sure to top up your account with enough found to buy the numbers
* Python 3
* Optional: set up OS variable environment with your Nexmo API key and secret

If you haven't set environment variables, replace os.getenv('nexmo_api_key') and os.getenv('nexmo_api_secret') with your API key and secret.

```python
params_keys = {
    'api_key': os.getenv('nexmo_api_key'),
    'api_secret': os.getenv('nexmo_api_secret')
}
```

# Use

## 1- Search Numbers (Search_Numbers.py)

* Upatde the settings to suit your needs
* `numberOfWantedNumbers` => indicates the number of phone numbers you're looking for
* `amountOfSequentialNumbers` => indicates how many sequential phone numbers you want 
* `country` => single value, must be using the ISO 2 country code
* `feature` => the phone number feature. `SMS` or `VOICE` or `VOICE,SMS`

```python
numberOfWantedNumbers = 10
amountOfSequentialsNumbers = 0

params_global = {
    'country': 'GB',
    # Possible values for features: SMS - VOICE - VOICE,SMS
    'features': 'SMS',
}
```

* Run the script: `python Search_Numbers.py`

## 2- Rent Numbers (Rent_Numbers.py)

* Upatde the settings to suit your needs
* `numberOfWantedNumbers` => indicates the number of phone numbers you're looking for
* `amountOfSequentialNumbers` => indicates how many sequential phone numbers you want 
* `country` => single value, must be using the ISO 2 country code
* `feature` => the phone number feature. SMS, VOICE, VOICE,SMS

```python
numberOfWantedNumbers = 10
amountOfSequentialsNumbers = 0

params_global = {
    'country': 'GB',
    # Possible values for features: SMS - VOICE - VOICE,SMS
    'features': 'SMS',
}
```

* Uncomment line 85: `#buyNumbers(country,msisdn)`
* Run the script: `python Rent_Numbers.py`

## 3- Search Owned Numbers (Search_Owned_Numbers.py)

* Upatde the settings to suit your needs
* `page_size` => indicates the number of phone numbers you want to display per page (max 100)
* `pattern` => indicates a pattern to search for. Use it to search number you own in a specific country 
* `search_pattern` => Strategy for matching pattern. Expected values: 0 (starts with, default), 1 (anywhere), 2 (ends with).

```python
page_size = 10          # default 10, max 100
pattern = ''            # A matching pattern (not required)
search_pattern = ''     # Strategy for matching pattern. Expected values: 0 (starts with, default), 1 (anywhere), 2 (ends with). (not required)
```

* Run the script: `python Search_Owned_Numbers.py`

## 4- Update Owned Numbers (Update_Owned_Numbers.py)

* Upatde the settings to suit your needs
* `page_size` => indicates the number of phone numbers you want to display per page (max 100)
* `pattern` => indicates a pattern to search for. Use it to update number(s) you own in a specific country 
* `search_pattern` => Strategy for matching pattern. Expected values: 0 (starts with, default), 1 (anywhere), 2 (ends with).
* `moHttpUrl` => An URL encoded URI to the webhook endpoint that handles inbound messages. Your webhook endpoint must be active before you make this request, Nexmo makes a GET request to your endpoint and checks that it returns a 200 OK response. Set to empty string to clear.
* `moSmppSysType` => The associated system type for your SMPP client. For example inbound
* `voiceCallbackValue has to be used together with voiceCallbackType parameter`
* `voiceCallbackType` => The voice webhook type. Possible values are sip, tel, or app
* `voiceCallbackValue` => A SIP URI, telephone number or Application ID
* `voiceStatusCallback` => A webhook URI for Nexmo to send a request to when a call ends.

```python
page_size = 5                # default 10, max 100
pattern = ''                 # A matching pattern (not required)
search_pattern = ''         # Strategy for matching pattern. Expected values: 0 (starts with, default), 1 (anywhere), 2 (ends with). (not required)

moHttpUrl = ''                  # moHttpUrl: An URL encoded URI to the webhook endpoint that handles inbound messages. Your webhook endpoint must be active before you make this request, Nexmo makes a GET request to your endpoint and checks that it returns a 200 OK response. Set to empty string to clear.
moSmppSysType = ''       # moSmppSysType: The associated system type for your SMPP client. For example inbound
# voiceCallbackValue has to be used together with voiceCallbackType parameter.
voiceCallbackType = ''    # voiceCallbackType: The voice webhook type. Possible values are sip, tel, or app
voiceCallbackValue = ''   # voiceCallbackValue: A SIP URI, telephone number or Application ID
voiceStatusCallback = ''   # voiceStatusCallback: A webhook URI for Nexmo to send a request to when a call ends.
```

* Run the script: `python Update_Owned_Numbers.py`

## 5- Cancel Owned Numbers (Cancel_Owned_Numbers.py)

* Upatde the settings to suit your needs
* `page_size` => indicates the number of phone numbers you want to display per page (max 100)
* `pattern` => indicates a pattern to search for. Use it to cancel number(s) you own in a specific country 
* `search_pattern` => Strategy for matching pattern. Expected values: 0 (starts with, default), 1 (anywhere), 2 (ends with).

BE CAREFULL WITH THE pattern and seach_pattern parameter as it will cancel ALL PHONE NUMBERS YOU OWN THAT MATCHES the pattern criteria. In the code it's set to cancel all Spanish Numbers.

```python
page_size = 5                # default 10, max 100
pattern = '34'                 # A matching pattern (not required)
search_pattern = '0'         # Strategy for matching pattern. Expected values: 0 (starts with, default), 1 (anywhere), 2 (ends with). (not required)

```

* Run the script: `python Cancel_Owned_Numbers.py`

Example: 
```console
python Cancel_Owned_Numbers.py
Cancelling {'country': 'ES', 'msisdn': '34911067079', 'moHttpUrl': 'http://madrid.nexmodemo.com/inbound', 'type': 'landline', 'metadata': [], 'features': ['SMS']}
Country ES, MSISDN 34911067079
{'api_secret': 'eab57dd40c2fd511', 'msisdn': '34911067079', 'api_key': '89345951', 'country': 'ES'}
200-success
Cancelling {'country': 'ES', 'msisdn': '34911067271', 'moHttpUrl': 'http://madrid.nexmodemo.com/contests', 'type': 'landline', 'metadata': [], 'features': ['SMS']}
Country ES, MSISDN 34911067271
{'api_secret': 'eab57dd40c2fd511', 'msisdn': '34911067271', 'api_key': '89345951', 'country': 'ES'}
200-success
```
