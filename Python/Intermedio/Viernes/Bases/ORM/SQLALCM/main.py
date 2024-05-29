from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
####
from sqlalchemy import Column, Integer, String, DateTime

# Configurar conexiones entre SQLAlchemy y SQLite3 DB API
engine = create_engine("sqlite:///BaseSQLALchemy.db")

# Crear sesión con el engine de base de datos
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Cancion(Base):

  __tablename__ = 'cancion'
  id = Column(Integer, primary_key=True)
  titulo = Column(String)
  minutos = Column(Integer)
  segundos = Column(Integer)
  compositor = Column(String)

  def __str__(self):
    return self.titulo

if __name__ == '__main__':
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    #song1 = Cancion(id= 1, titulo ="F", minutos = "s")
    #session.add(song1)
    #session.commit()

    songs = session.query(Cancion).all()

    for song in songs:
        print(song)

