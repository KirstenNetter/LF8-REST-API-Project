from main import getData

data = getData().json()



if data["cod"] != "404":
   

    current_temperature = data['main']['temp']
    current_weather = data['']


print(current_weather)