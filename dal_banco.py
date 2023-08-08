from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.reflection import Inspector


def Criar_tabelas():

    session, engine = Retorna_Session()
    inspector = Inspector.from_engine(engine)

    Base = declarative_base()
    try:
        if 'Usuario' not in inspector.get_table_names():
            class Usuario(Base):
                __tablename__ = "Usuario"
                id = Column(Integer, primary_key=True)
                nome = Column(String(60))
                email= Column(String(50))        
                senha = Column(String(80))

            Base.metadata.create_all(engine)

        session.commit()
        session.close()
    except Exception as e:
        session.rollback()
        print(f"Erro ao Criar tabela :{e} ")
    finally:
        session.close()

def Retorna_Session():
    USUARIO = 'root'
    SENHA = ""
    HOST = "localhost"
    BANCO = "Mercearia"
    PORT = "3306"
    
    CONN = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"

    engine = create_engine(CONN, echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session, engine

def FecharSession(user):
    user.close()
