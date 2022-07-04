import requests

def triviaGeneral():
    


    category = 'general'

    api_url = 'https://api.api-ninjas.com/v1/trivia?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': '+vI+MmL3KPXWtMi1afgp/g==KxSX8Ph9oTmbmUIE'})
    if response.status_code == requests.codes.ok:
       return (response.text)
    else:
        return("Error:", response.status_code, response.text)
    
print(triviaGeneral())