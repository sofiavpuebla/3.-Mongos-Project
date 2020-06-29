import pandas as pd
import requests
import json
from dotenv import load_dotenv
import os

def GetFromFourSquare(query):
    url = 'https://api.foursquare.com/v2/venues/explore'
    params = dict(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    v='20180323',
    ll='25.7722,-80.1867',
    query=f'{query}',
    limit=100
    )
    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)["response"]["groups"][0]["items"]
    return data

def getInfo(category):
    data=[]
    for i in range(len(category)):
        item={"id":category[i]["venue"]["id"],
                "name":category[i]["venue"]["name"],
                "lat":category[i]["venue"]["location"]["lat"],
                "lng":category[i]["venue"]["location"]["lng"]
                }
        
        data.append(item)
        
    return pd.DataFrame(data)

