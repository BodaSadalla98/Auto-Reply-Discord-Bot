import weakref
import requests
import json
import  wikipedia
from requests.api import get, head
from wikipedia.wikipedia import summary

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

def get_wiki_url(keyword):
    keyword = keyword.replace(' ','')
    page = wikipedia.page(keyword)

    url = None

def get_wiki_image(keyword):
    try:
        url = 'https://en.wikipedia.org/w/api.php'
        data = {
            'action' :'query',
            'format' : 'json',
            'formatversion' : 2,
            'prop' : 'pageimages',
            'piprop' : 'thumbnail',
            'titles' : keyword
        }
        response = requests.get(url, data)
        json_data = json.loads(response.text)
        image = json_data['query']['pages'][0]['thumbnail']['source']  if 'thumbnail' in json_data['query']['pages'][0] else None

    except:
        image = None
    return image

def get_wiki_summary(keyword):
    ret = ''
    keyword= keyword.replace(' ', '')
    try:
        
        ret = wikipedia.summary(keyword,auto_suggest = True, redirect = True, chars=2000)
        
    except:
        ret =  None
        
    
    

    return ret
   

def get_wiki(keyword):
    ret = ''
    original = keyword
    image = get_wiki_image(keyword)
    keyword= keyword.replace(' ', '')
    summary = get_wiki_summary(keyword)
    try:
        page = wikipedia.page(keyword, auto_suggest=True, redirect=True, preload=False)
        if summary is None:
            summary = page.summary[:2000]
        url = page.url
        title = page.title
        
    except:
         summary =  'Either This Page Doesn\'t Exist, or you need to be more specific'
         url= None
         title = None
    if title is None:
        title = original

    return title,summary,url, image

#print(get_wiki('naruto anime'))

#print (get_wiki_summary('naruto anime'))
#print(wikipedia.page('wikipedia').images[0])
