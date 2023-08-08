from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from dal_banco import Retorna_Session

session = Retorna_Session()
Base = declarative_base()
    
class Usuario(Base):
    __tablename__ = "Usuario"
    id = Column(Integer, primary_key=True)
    nome = Column(String(60))
    email= Column(String(50))        
    senha = Column(String(80))  