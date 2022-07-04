import requests
import  json

def randomFactCall():

    limit = 1
    api_url = 'https://api.api-ninjas.com/v1/facts?limit={}'.format(limit)
    response = requests.get(api_url, headers={'X-Api-Key': 'your api key here'})
    if response.status_code == requests.codes.ok:
        res = response.text
        loadRes = json.loads(res)
        resInd = loadRes[0]
        factRes = resInd['fact']
        return factRes
    else:
        return ("Error:", response.status_code, response.text)
    
    
    
print(randomFactCall())
