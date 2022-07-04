import requests
import json


def jokeCall():

    limit = 1
    api_url = 'https://api.api-ninjas.com/v1/jokes?limit={}'.format(limit)
    response = requests.get(api_url, headers={'X-Api-Key': '+vI+MmL3KPXWtMi1afgp/g==KxSX8Ph9oTmbmUIE'})
    if response.status_code == requests.codes.ok:
        res = response.text
        res = response.text
        loadRes = json.loads(res)
        resInd = loadRes[0]
        jokeRes = resInd['joke']
        return jokeRes
        
    else:
        return ("Error:", response.status_code, response.text)
    

print(jokeCall())