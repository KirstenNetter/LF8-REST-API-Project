import requests



api_url = 'http://api.openweathermap.org/data/2.5/weather'
appid = '37ff124f7b9731863a401cbb9b89e396' 
r = requests.get(url=api_url, params=dict(q='Berlin',main ='Metric' ,APPID=appid))

#print(r)

for entry in r:
    
    print(entry)


