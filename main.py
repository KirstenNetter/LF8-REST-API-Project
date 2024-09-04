import requests


api_url = 'http://api.openweathermap.org/data/2.5/weather'
appid = '37ff124f7b9731863a401cbb9b89e396'


einheit = 'metric'

def getData(ort):
    response = requests.get(url=api_url, params=dict(q=ort, APPID=appid, units=einheit))
    return response







