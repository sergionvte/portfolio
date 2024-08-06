import requests
import json
def check_mail(email):
    url = "https://email-checker.p.rapidapi.com/verify/v1"
    querystring = {"email": email}
    headers = {
        "X-RapidAPI-Key": "af6772b899msh3cc9dc6dc67cb31p152357jsnbe18f5a697a5",
        "X-RapidAPI-Host": "email-checker.p.rapidapi.com"
    }
    response = requests.request(
        "GET", url, headers = headers, params = querystring
    )
    values = json.loads(response.text)

    print(values)

    return True if values['status'] == 'valid' else False
