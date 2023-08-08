from  model   import Usuario
import hashlib

class DalUsusario:    
    @classmethod
    def ler_usuario(cls, codigo, email, session):
        try:                
            if codigo ==9999:
                vUsuario= session.query(Usuario).filter(Usuario.id > 0).all()
            elif email =='':
                vUsuario= session.query(Usuario).filter(Usuario.id == int(codigo)).first()
            else: vUsuario = session.query(Usuario).filter(Usuario.email == email, Usuario.id != codigo).first()

            return vUsuario
        except Exception as e:
            session.rollback()  
            print("Erro durante a leitura do usuário:", str(e))
            x=input()
            
    @classmethod
    def incluir(cls, vUsuario, session):
        try:    
            session.add(vUsuario)
            session.commit()
        except Exception as e:
            session.rollback()  
            print("Erro durante a inclusão do usuário:", str(e))
            x=input()

    @classmethod
    def alteracao(cls, vUsuario, session):
        try:
            session.commit() 
        except Exception as e:
            session.rollback()  
            print("Erro durante a alteração do usuário:", str(e))
            x=input()

    @classmethod
    def excluir(cls, vUsuario, session):
        try:
            session.delete(vUsuario)
            session.commit() 
        except Exception as e:
            session.rollback()  
            print("Erro durante a exclusao do usuário:", str(e))
            x=input()

