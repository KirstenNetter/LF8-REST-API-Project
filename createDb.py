from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import Column, ForeignKey
from sqlalchemy.sql.sqltypes import String, Integer, Float


engine = create_engine('sqlite:///database.db')
base = declarative_base()
conn = engine.connect()
Session = sessionmaker()


class Wetterlage(base):
    __tablename__ = 'wetterlagen'

    ort_id = Column(Integer, ForeignKey('orte.ort_id'), primary_key=True)
    zeit = Column(Integer, ForeignKey('zeiten.zeit'), primary_key=True)
    temperatur = Column(Float, nullable=False)
    luftdruck = Column(Integer, nullable=False)
    Bewoelkungsgrad = Column(Integer, nullable=False)
    wettertyp_id = Column(Integer, ForeignKey('wettertypen.wettertyp_id'), nullable=False)

    def __init__(self, temperatur, luftdruck, bewoelkungsgrad) -> None:
        self.temperatur = temperatur
        self.luftdruck = luftdruck
        self.bewoelkungsgrad = bewoelkungsgrad


class Wettertyp(base):
    __tablename__ = 'wettertypen'

    wettertyp_id = Column(Integer, primary_key=True, autoincrement=True)
    typ = Column(String, nullable=False)

    def __init__(self, typ) -> None:
        self.typ = typ


class Ort(base):
    __tablename__ = 'orte'

    ort_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    def __init__(self, name) -> None:
        self.name = name


class Zeit(base):
    __tablename__ = 'zeiten'

    zeit = Column(Integer, primary_key=True, autoincrement=True)



base.metadata.create_all(conn)
