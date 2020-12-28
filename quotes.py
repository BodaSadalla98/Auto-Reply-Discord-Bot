import requests
import json

from requests.api import get, head

def get_quote():
    response = requests.get("https://api.quotable.io/random")
    if response.ok:
        data = json.loads(response.text)
        quote = data['content']
        author = data['author']
        return  (f' {quote} - {author}')
        


def get_dad_joke():
    respone = requests.get("https://icanhazdadjoke.com/", headers={'Accept': 'application/json'})
    if respone.ok:
        respone = respone.json()
        respone = respone['joke']
        return respone


def get_joke():
    url = "https://joke3.p.rapidapi.com/v1/joke"
    querystring = {"nsfw":"true"}
    headers = {
        'x-rapidapi-key': "f9c6b4ead7mshb8f34698e1f16e0p123739jsn451f75309298",
        'x-rapidapi-host': "joke3.p.rapidapi.com"
        }
    good = 0
    bad = 0
    while good <= bad:
        response = requests.request("GET", url, headers=headers)
        if response.ok:
            data = response.json()
            good = data['upvotes'] 
            bad = data['downvotes']
            if good > bad :
                return data['content']



   

