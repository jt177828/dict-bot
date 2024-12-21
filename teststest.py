from ast import Return
import json
import requests


def url(word):
    return("https://dictionaryapi.com/api/v3/references/collegiate/json/{word}?key=23bbc9d1-539a-4827-94a2-ee37eb6ee1c1")


response = requests.get(f"https://dictionaryapi.com/api/v3/references/collegiate/json/{}?key=23bbc9d1-539a-4827-94a2-ee37eb6ee1c1",
                        headers={'app_id': '8b220f60', 'app_key': '23bbc9d1-539a-4827-94a2-ee37eb6ee1c1'})
print(response.status_code)


array = response.json()
print(array)
