# python-number
Use the Nexmo's API to check phone numbers availability or rent them 

Pre-requisites
- open a Nexmo account
- make sure to top up your account with enough found to buy the numbers
- Python 3
- Optional: set up OS variable environment with your Nexmo API key and secret

Use

If you haven't set environment variables, replace os.getenv('nexmo_api_key') and os.getenv('nexmo_api_secret') with your API key and secret.

params_keys = {
    'api_key': os.getenv('nexmo_api_key'),
    'api_secret': os.getenv('nexmo_api_secret')
}

1- Search Numbers (Search_Numbers.py)

- Upatde the settings to suit your needs
- numberOfWantedNumbers => indicates the number of phone numbers you're looking for
- amountOfSequentialNumbers => indicates how many sequential phone numbers you want 
- country => single value, must be using the ISO 2 country code
- feature => the phone number feature. SMS, VOICE, VOICE,SMS

numberOfWantedNumbers = 10
amountOfSequentialsNumbers = 0

params_global = {
    'country': 'GB',
    # Possible values for features: SMS - VOICE - VOICE,SMS
    'features': 'SMS',
}

- Run the script: python Search_Numbers.py

2- Rent Numbers (Rent_Numbers.py)

- Upatde the settings to suit your needs
- numberOfWantedNumbers => indicates the number of phone numbers you're looking for
- amountOfSequentialNumbers => indicates how many sequential phone numbers you want 
- country => single value, must be using the ISO 2 country code
- feature => the phone number feature. SMS, VOICE, VOICE,SMS

numberOfWantedNumbers = 10
amountOfSequentialsNumbers = 0

params_global = {
    'country': 'GB',
    # Possible values for features: SMS - VOICE - VOICE,SMS
    'features': 'SMS',
}

- Uncomment line 85: #buyNumbers(country,msisdn)
- Run the script: python Rent_Numbers.py
