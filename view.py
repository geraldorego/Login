import os.path
from termcolor import colored
from controller import ConfirmacaoControler, UsuarioControler, SenhaControler
import getpass

ConfirmacaoControler.criaArquivo()

if __name__ == "__main__":
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print (colored('=========== MODULO DE LOGIN ===========\n','red', attrs=['bold']))
        
        modulo = input(colored('Opção :  1 - Cadastro de Usuário \n'
                            '          2 - Login                  \n' 
                            '          0 - Finalizar Sistema      \n'
                            'Informe a Opção :','blue', attrs=['bold']
                            )
                    )
                
        while not modulo.isnumeric():
            modulo = input(colored('Digite um opcão válida: ','yellow'))

        modulo=ConfirmacaoControler.opcao_valida(modulo,2)
        modulo=int(modulo)                           

        if modulo==1:     #===================== Usuario =============================
            msg=''
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')

                print ('=========== CADASTRO DE USUARIO =========== ')
                print (colored('==== Digite <9999> para Listar Todos Usuarios ==','yellow'))
                opcao = input(colored('Opção :  1 - INCLUIR \n'
                                    '          2 - ALTERAR \n' 
                                    '          3 - EXCLUIR \n'
                                    '          0 - Sair    \n'
                                    'Informe a Opção :','blue', attrs=['bold']
                            )
                    )
                nome=''
                email=''
                senha=''
                opcao = ConfirmacaoControler.opcao_valida(opcao, 4)
                if opcao==0: break

                if opcao > 1:    
                    codigo =input('Codigo do Usuario : ')
                    codigo = ConfirmacaoControler.opcao_valida(codigo, 9999)                  
                    vUsuario, session, codigo = UsuarioControler.pesquisa_usuario(codigo)
                    
                    if codigo == 0: break
                    if not vUsuario:
                        x=input('=== Usuario Não cadastrado, retorne para Inclusão === < Tecle Enter >') 
                        continue
                    else:
                        nome =vUsuario.nome
                        email=vUsuario.email
                        x=input(f'aqui   {codigo} - {opcao}')
                        if opcao == 2:
                            msg='Alteração'
                            nome = input(colored(f' Nome   : {nome}  - Novo : ','blue'))
                            email= input(colored(f' E-mail : {email} - Novo : ','blue'))   
                            while True:
                                vemail=UsuarioControler.pesquisa_email(codigo,email)
                                if  vemail:
                                    print(colored(f' E-mail ja cadastrado! digite outro','blue'))   
                                else: break
                                email = input(colored(f' E-mail : {email} - Novo : ','blue'))   

                            senha = getpass.getpass(colored(f'Senha ********** - Nova : ','blue'))
                            senha = SenhaControler.valida_senha(senha)
                            senha = UsuarioControler.criptografar_senha(senha)

                        elif opcao==3:
                            msg='Exclusão'
                            print(colored(f' Nome   : {nome}','blue'))
                            print(colored(f' E-mail : {email}','blue'))   

                        conf =  ConfirmacaoControler.confirmacao(msg)
                        if conf=='S':
                            vUsuario.nome = nome
                            vUsuario.email = email
                            vUsuario.senha = senha
                            UsuarioControler.manutencao_usuario(msg, vUsuario, session)  
                elif opcao ==1:     
                    msg='Inclusao'      
                    nome = input(colored(f' Nome   : ','blue'))
                    email= input(colored(f' E-mail : ','blue'))
                    while True:
                        vemail=UsuarioControler.pesquisa_email(0,email)
                        if  vemail:
                            x=input(colored(f' E-mail ja cadastrado! digite outro','blue'))   
                        else: break
                        email= input(colored(f' E-mail : {email} - Novo : ','blue'))   

                    senha = getpass.getpass(colored(f'Digite sua senha: ','blue'))
                    senha = SenhaControler.valida_senha(senha)
                    senha = UsuarioControler.criptografar_senha(senha)
                    conf =  ConfirmacaoControler.confirmacao(msg)   
                    if conf=='S':
                        UsuarioControler.inclusao_usuario(msg, nome, email, senha)  

        elif modulo==2:
            os.system('cls' if os.name == 'nt' else 'clear')

            print (colored('========== LOGIN NO SISTEMA =========== ','blue'))
            print (colored('E-mail : vazio <Encerra>  ','blue'))

            email= input(colored(f' E-mail : ','green'))   
            senha = getpass.getpass(colored(f'Senha : ','green'))
            senha = UsuarioControler.criptografar_senha(senha)
            vemail=UsuarioControler.pesquisa_email(0, email)
            if not vemail:
                 x=input(colored('Email não Cadastrado! ','yellow'))
            elif  vemail.senha != senha:
                  x=input(colored('Senha não confere! ','yellow'))
            else:   
                x=input(colored('LOGIN COM SUCESSO! ','green'))
                break

        else: break  