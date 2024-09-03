from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import Column, ForeignKey
from sqlalchemy.sql.sqltypes import String, Integer, Float
from sqlalchemy.sql.sqltypes import DateTime





engine = create_engine('sqlite:///database.db')
base = declarative_base()


 



class Wetterlage(base):
    __tablename__ = 'wetterlagen'

    ort_id = Column(Integer, ForeignKey('orte.ort_id'), primary_key=True,nullable=False)
    zeit = Column(String, ForeignKey('zeiten.zeit'), primary_key=True,nullable=False)
    temperatur = Column(Float, nullable=False)
    luftdruck = Column(Integer, nullable=False)
    bewoelkungsgrad = Column(Integer, nullable=False)
    wettertyp_id = Column(Integer, ForeignKey('wettertypen.wettertyp_id'), nullable=False)
  

    ort = relationship("Ort", back_populates="wetterlagen")
    zeit_obj = relationship("Zeit", back_populates="wetterlagen")
    wettertyp = relationship("Wettertyp", back_populates="wetterlagen")


    def __init__(self, temperatur, luftdruck, bewoelkungsgrad,weathertyp_id,ort,zeit_obj,wettertyp) -> None:
        self.temperatur = temperatur
        self.luftdruck = luftdruck
        self.bewoelkungsgrad = bewoelkungsgrad
        self.wettertyp_id=weathertyp_id
        self.ort=ort
        self.zeit_obj=zeit_obj
        self.wettertyp=wettertyp




class Wettertyp(base):
    __tablename__ = 'wettertypen'

    wettertyp_id = Column(Integer, primary_key=True, autoincrement=False)
    typ = Column(String, nullable=False)
    wetterlagen = relationship("Wetterlage", back_populates="wettertyp")
    def __init__(self, typ,wettertyp_id) -> None:
        self.typ = typ
        self.wettertyp_id=wettertyp_id





class Ort(base):
    __tablename__ = 'orte'

    ort_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    wetterlagen = relationship("Wetterlage", back_populates="ort")
    def __init__(self, name,ort_id) -> None:
        self.name = name
        self.ort_id=ort_id



class Zeit(base):
    __tablename__ = 'zeiten'

    zeit = Column(DateTime, primary_key=True, autoincrement=False)
    wetterlagen = relationship("Wetterlage", back_populates="zeit_obj")
    def __init__(self,zeit)->None:
        self.zeit=zeit



base.metadata.create_all(bind=engine)
conn = engine.connect()
Session = sessionmaker(bind=engine)
