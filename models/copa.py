from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base 

class Copa(Base):
    __tablename__ = 'copas'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    precio_publico = Column(Float, nullable=False)
    tipo_vaso = Column(String, nullable=False)
    ingrediente_1_id = Column(Integer, ForeignKey('ingredientes.id'))
    ingrediente_2_id = Column(Integer, ForeignKey('ingredientes.id'))
    ingrediente_3_id = Column(Integer, ForeignKey('ingredientes.id'))
    ingrediente_1 = relationship("Ingrediente", foreign_keys=[ingrediente_1_id])
    ingrediente_2 = relationship("Ingrediente", foreign_keys=[ingrediente_2_id])
    ingrediente_3 = relationship("Ingrediente", foreign_keys=[ingrediente_3_id])
