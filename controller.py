import hashlib
import re
import getpass
from dal_banco import Retorna_Session, Criar_tabelas
from termcolor import colored
from operator import itemgetter
from  model   import Usuario
from  dal     import DalUsusario

class ConfirmacaoControler:

    @classmethod  
    def criaArquivo(cls):
        Criar_tabelas()

    @classmethod     
    def confirmacao(cls, msg):
        conf=''
        while conf.upper() not in ('S','N'):
            conf=input(colored(f'{msg}  [S/N]' ,'cyan', attrs=['bold']))
        
        return conf.upper()

    @classmethod
    def numero_valido(cls, campo):
         
        while not campo.isnumeric():
            campo = input(colored('Digite um número válido: ','yellow'))

        campo2=int(campo)
        return campo2    
    
    @classmethod
    def opcao_valida(cls, campo,num):
        while True: 
            if not campo.isnumeric():
                campo = input(colored('Digite um número válido: ','yellow'))

            campo2=int(campo)
            if campo2 > num:
                campo = input(colored('Digite a Opçaõ correta : ','yellow'))
            else: break

        return campo2   
    @classmethod
    def senha_contem_caracteres_especiais(cls, senha):
        # Definir a expressão regular para procurar caracteres especiais
        padrao = r"[!@#$%^&*(),.?\":{}|<>]"

        if re.search(padrao, senha):
            return True
        else:
            return False
        
    @classmethod
    def senha_contem_letra_maiuscula(cls, senha):
        padrao = r"[A-Z]"
        if re.search(padrao, senha):
            return True
        else:
            return False

class SenhaControler:

    @classmethod
    def valida_senha(cls, senha):
        while True:          
            if len(senha) < 8:
                x=input(colored('Senha menor que 8 caracteres','blue')) 
            elif not ConfirmacaoControler.senha_contem_caracteres_especiais(senha):
                x=input(colored('Seha precisa ter um caracter especial','blue'))      
            elif not ConfirmacaoControler.senha_contem_letra_maiuscula(senha):
                x=input(colored('Seha precisa ter um Letra Maiuscula','blue'))                
            else: break    

            senha = getpass.getpass(colored(f'Digite sua senha: ','blue'))
        return senha
    
class UsuarioControler:

    @classmethod
    def pesquisa_email(cls, codigo, email):
        session, x = Retorna_Session()
        vUsuario=DalUsusario.ler_usuario (codigo, email, session)

        return vUsuario

    @classmethod
    def pesquisa_usuario(cls, codigo):
        session, x = Retorna_Session()
        while True:
            if codigo == 9999:
                vUsuario=DalUsusario.ler_usuario (codigo,'',session)
                UsuarioControler.lista_Usuario(vUsuario)
            else:                
                vUsuario=DalUsusario.ler_usuario (codigo, '', session)
                return vUsuario, session, codigo

            codigo =input('Codigo do Usuario : ')
            codigo =ConfirmacaoControler.opcao_valida(codigo,9999) 
    
    @classmethod
    def inclusao_usuario(cls, msg, nome, email, senha):
        session, x = Retorna_Session()
        try:            
            vUsuario = Usuario(nome=nome, email=email, senha=senha)
            session.add(vUsuario)  
            DalUsusario.incluir(vUsuario, session)
        except Exception as e:
            session.rollback()  
            print("Erro durante a inclusão do usuário:", str(e))
            x=input()

    @classmethod
    def manutencao_usuario(cls, msg, vUsuario, session):
        try:
            if  msg=='Alteração':
                DalUsusario.alteracao(vUsuario, session)
            else: DalUsusario.excluir(vUsuario, session)
        except Exception as e:
            session.rollback()  
            print("Erro durante a atualização do usuário:", str(e))
            x=input()

    @classmethod    
    def lista_Usuario(cls, vUsuario):
        for y in vUsuario:           
            print(colored(f'Usuario: {y.id} email : {y.email} nome : {y.nome}' ,'light_green'))

    @classmethod
    def criptografar_senha(cls, senha: str):
        return hashlib.sha256(senha.encode()).hexdigest()