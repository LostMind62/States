import requests
import json
import time
import numpy as np
import pandas as pd
import hashlib
from datetime import datetime
#Africa, Americas, Asia, Europe, Oceania
def get_response_region(region):
    response = requests.get("https://restcountries.com/v3.1/region/"+region)
    if response.status_code == 200:
        response = response.json()
    else:
        response = []
    return response

def get_lenguage(response):
    dict_lng=""
    if response['languages']:
        lng=list(response['languages'].keys())
        for x in lng:
            leng = response['languages'].get(x)
            dict_lng =dict_lng +","+leng
    else:
        dict_lng=""
    return dict_lng

def datas(response):
    # rows=pd.DataFrame(columns=['region', 'city name', 'Lenguaje','Time'])
    rows=[]
    tiempo = lambda x:  float(datetime.now().strftime('%S.%f')) - float(x.strftime('%S.%f'))
    if response != []:
        for x in response:
            dt = datetime.now()
            a=get_lenguage(x).encode()
            hash_object = hashlib.sha1(a).hexdigest()
            time.sleep(.00000000000000000000000000002)
            row= {
                'region' :x['region'],
                'city name' :x['name']['official'],
                'Lenguaje' :hash_object,
                'Time': tiempo(dt),
            }
            rows.append(row)
    else:
        rows = []
    return rows
        
           
if __name__ =="__main__":
    region=[ "Africa", "Americas", "Asia", "Europe", "Oceania"]
    results = []
    for a in region:
        response=get_response_region(a)
        result = datas(response)
        results.append(result)    
    result = pd.DataFrame(results, index=list(range(len(results))))

        # res = pd.concat([res, result])