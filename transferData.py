from main import getData
import time

data = getData().json()



if data["cod"] != "404":
   

    current_temperature = data['main']['temp']
    current_weather = data['weather'][0]['main']
    current_pressure = data['main']['pressure']
    current_cloudiness = data['clouds']['all']
    timecode = data['dt']
    current_time = time.ctime(timecode)

print(current_weather,current_pressure, current_cloudiness,current_time)