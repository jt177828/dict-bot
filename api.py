import requests
import json
# TODO: replace with your own app_id and app_key
app_id = '8b220f60'
app_key = '637ff7cff86b8c7e45c709032d8586c0'
language = 'en-gb'
word_id = 'Ace'
url = 'https://od-api.oxforddictionaries.com/api/v2/entries/' + \
    language + '/' + word_id.lower()
r = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})
print("code {}\n".format(r.status_code))
print("text \n" + r.text)
print("json \n" + json.dumps(r.json()))


print("text \n" + json.dumps(r.json()))
print(dict['id'])
print(dict['metadata']["operation"])
