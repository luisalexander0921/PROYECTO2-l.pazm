from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Ingrediente(Base):
    __tablename__ = 'ingredientes'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    precio = Column(Float, nullable=False)
    calorias = Column(Integer, nullable=False)
    es_vegetariano = Column(Boolean, nullable=False)
    copas = relationship('Copa', back_populates='ingrediente_1')  # Ajuste de relación
    malteadas = relationship('Malteada', back_populates='ingrediente_1')  # Ajuste de relación

class Copa(Base):
    __tablename__ = 'copas'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    precio_publico = Column(Float, nullable=False)
    tipo_vaso = Column(String, nullable=False)
    ingrediente_1_id = Column(Integer, ForeignKey('ingredientes.id'), nullable=True)
    ingrediente_2_id = Column(Integer, ForeignKey('ingredientes.id'), nullable=True)
    ingrediente_3_id = Column(Integer, ForeignKey('ingredientes.id'), nullable=True)
    ingrediente_1 = relationship("Ingrediente", foreign_keys=[ingrediente_1_id])
    ingrediente_2 = relationship("Ingrediente", foreign_keys=[ingrediente_2_id])
    ingrediente_3 = relationship("Ingrediente", foreign_keys=[ingrediente_3_id])

class Malteada(Base):
    __tablename__ = 'malteadas'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    precio_publico = Column(Float, nullable=False)
    volumen = Column(Integer, nullable=False)
    ingrediente_1_id = Column(Integer, ForeignKey('ingredientes.id'), nullable=True)
    ingrediente_2_id = Column(Integer, ForeignKey('ingredientes.id'), nullable=True)
    ingrediente_3_id = Column(Integer, ForeignKey('ingredientes.id'), nullable=True)
    ingrediente_1 = relationship("Ingrediente", foreign_keys=[ingrediente_1_id])
    ingrediente_2 = relationship("Ingrediente", foreign_keys=[ingrediente_2_id])
    ingrediente_3 = relationship("Ingrediente", foreign_keys=[ingrediente_3_id])

# Configuración de la base de datos
engine = create_engine('sqlite:///heladeria.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
