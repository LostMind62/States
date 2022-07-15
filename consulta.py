import requests
import json
import time
from pandas import DataFrame as df
#Africa, Americas, Asia, Europe, Oceania
# json_formatted_str = json.dumps(response[0], indent=2)
def get_response_region(region):
    response = requests.get("https://restcountries.com/v3.1/region/"+region)
    if response.status_code == '200':
        response = response.json()
    else:
        response = []
    return response

def get_lenguage(response):
    dict_lng=[]
    if response['languages']:
        lng=list(response['languages'].keys())
        for x in lng:
            leng = response['languages'].get(x)
            dict_lng.append(leng)
    else:
        dict_lng=[]
    return dict_lng

def datas(response):
    b=[]
    a=[]
    if response != []:
        for x in response:
            a= {
                'region' :x['region'],
                'city name' :x['name']['official'],
                'Lenguaje' :get_lenguage(x),
            }
            b.append(a)
        return b
    else:
        b = [] 
        
           
if __name__ =="__main__":
    region=[ "Africa", "Americas", "Asia", "Europe", "Oceania"]
    for a in region:
        response=get_response_region(a)
        result = datas(response)
    

# for x in response:
    # print(x['name']['common'])
    # print(x['region']['common'])