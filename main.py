import requests



api_url = 'http://api.openweathermap.org/data/2.5/weather'
appid = '37ff124f7b9731863a401cbb9b89e396' 

def getData():
    response = requests.get(url=api_url, params=dict(q='Berlin' ,APPID=appid,  units='metric'))
    return response


#print(r)
#Temperatur, Datum, Wetter, Ort





