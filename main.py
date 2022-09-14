import requests;from requests.structures import CaseInsensitiveDict;import json;url = "https://api.currencyapi.com/v3/latest";print('\n\nWhat currencies do you want to compare?\nIt will be compared to 1 USD');currency_to = str(input('e.g "GBP":    '));headers = CaseInsensitiveDict();print(headers);headers["apikey"] = "hPChnKc6Fm90OaX4rMjezi847Gy2j4qZMhFC1iBk";headers["currencies"] = currency_to;print(headers);resp = requests.get(url, headers=headers);respons = resp.text;jsonData = json.loads(resp.text);print(jsonData);jsonData = jsonData['data']
try:jsonData = jsonData[currency_to]
except:
    print('Not found in database')
else:
    final = jsonData['value']
    print('\n\n\n######################################################\n\n\n' + str(final) + '\n\n\n######################################################')