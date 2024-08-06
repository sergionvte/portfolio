from portfolio.settings import XRAPIDAPIKEY
import requests
import json
def check_mail(email):
    url = "https://email-checker.p.rapidapi.com/verify/v1"
    querystring = {"email": email}
    headers = {
        "X-RapidAPI-Key": XRAPIDAPIKEY,
        "X-RapidAPI-Host": "email-checker.p.rapidapi.com"
    }
    response = requests.request(
        "GET", url, headers = headers, params = querystring
    )
    values = json.loads(response.text)

    print(values)

    return True if values['status'] == 'valid' else False
