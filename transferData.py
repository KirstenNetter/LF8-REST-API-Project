from main import getData
from datetime import datetime
from createDb import Session, engine,Wetterlage,Wettertyp,Ort,Zeit

data = getData().json()



my_Session = Session(bind=engine)



if data["cod"] != "404":
   
    name = data['name']
    ort_id = data['id']
    ort=Ort(name,ort_id)
    if not my_Session.query(Ort).filter(Ort.ort_id==ort_id):
        my_Session.add(ort)
    

    timecode = data['dt']
    current_time = datetime.fromtimestamp(timecode)
    zeit=Zeit(current_time)
    my_Session.add(zeit)

    current_weather = data['weather'][0]['main']
    weather_id = data['weather'][0]['id']
    wettertyp=Wettertyp(current_weather,weather_id)
    my_Session.add(wettertyp) 


    current_temperature = data['main']['temp']
    current_pressure = data['main']['pressure']
    current_cloudiness = data['clouds']['all']
    wetterlage=Wetterlage(current_temperature,current_pressure,current_cloudiness,weather_id,ort,zeit,wettertyp)
    my_Session.add(wetterlage)

    my_Session.commit()



    






print(name,id,weather_id)