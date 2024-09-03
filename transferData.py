from main import getData
from datetime import datetime
from createDb import Session, engine, Wetterlage, Wettertyp, Ort, Zeit
from sqlalchemy import select, exists
from sqlalchemy.orm import Session

data       = getData().json()
my_Session = Session(bind=engine)


if data["cod"] != "404":
   
    name         = data['name']
    ort_id       = data['id']
    exists_query = select(exists().where(Ort.ort_id == ort_id))
    result       = my_Session.execute(exists_query).scalar()

    if not result:
        ort = Ort(name, ort_id)
        my_Session.add(ort)
        my_Session.flush()
    else:
        ort = my_Session.query(Ort).filter_by(ort_id=ort_id).one()
        
    timecode     = data['dt']
    current_time = datetime.fromtimestamp(timecode)
    exists_query = select(exists().where(Zeit.zeit == current_time))
    result       = my_Session.execute(exists_query).scalar()

    if not result:
        zeit = Zeit(current_time)
        my_Session.add(zeit)
        my_Session.flush()  
    else:
        zeit = my_Session.query(Zeit).filter_by(zeit=current_time).one()

    
    current_weather = data['weather'][0]['main']
    weather_id      = data['weather'][0]['id']
    exists_query    = select(exists().where(Wettertyp.wettertyp_id == weather_id))
    result          = my_Session.execute(exists_query).scalar()

    if not result:
        wettertyp = Wettertyp(current_weather, weather_id)
        my_Session.add(wettertyp)
        my_Session.flush()  
    else:
        wettertyp = my_Session.query(Wettertyp).filter_by(wettertyp_id=weather_id).one()

    current_temperature = data['main']['temp']
    current_pressure    = data['main']['pressure']
    current_cloudiness  = data['clouds']['all']

    wetterlage = Wetterlage(
        temperatur=current_temperature,
        luftdruck=current_pressure,
        bewoelkungsgrad=current_cloudiness,
        weathertyp_id=weather_id,
        ort=ort,
        zeit_obj=zeit,
        wettertyp=wettertyp
    )
    my_Session.add(wetterlage)
    my_Session.commit()

