class Pessoa():
    def __init__(self,nome,cep,cidade,endereco,tel,cpf,rg,user,senha):
        self.__nome = input("Digite seu nome: ")
        self.__cep = input("Digite seu cep: ")
        self.__cidade = input("Digite seu cidade: ")
        self.__endereco = input("Digite seu endereço: ")
        self.__tel = input("Digite seu telefone: ")
        self.__cpf = input("Digite seu cpf: ")
        self.__rg = input("Digite seu rg: ")
        self.__id = int(input("Digite seu id: "))
        self.__user = input("Digite seu nome de usuario: ")
        self.__senha = input("Digite sua senha: ")

    def getUser(self):
        return self.__user

    def getSenha(self):
        return self.__senha

    def logar(self,user,senha):
        if senha != self.getSenha():
            print("Senha Incorreta")
        elif user != self.getUser():
            print("Usuario Incorreta")
        else:
            print(f"Usuario {user} logado com sucesso!")
    
class Cliente(Pessoa):
    def __init__(self):
        pass

    def trocarSenha(self,senha):
        self.__senha = senha
        print("Senha alterada com sucesso!")
        return senha
        
    def deletarUser():
        del Cliente
        print("Conta deletada com sucesso!")

    def alterarDados(self):
        resposta = int(input("""
        Se quiser alterar o nome digite 1
        Se quiser alterar cep digite 2
        Se quiser alterar cidade digite 3
        Se quiser alterar endereco digite 4
        Se quiser alterar telefone digite 5
        Se quiser alterar cpf digite 6
        Se quiser alterar rg digite 7
        Se quiser alterar usuario digite 8
        Se quiser alterar senha digite 9
        """))

        match resposta:
    
            #nome
            case 1:
                self.__nome = input("Digite seu novo nome: ")
            
            #cep
            case 2:
                self.__cep = input("Digite seu novo cep: ")
            
            #cidade
            case 3:
                self.__cidade = input("Digite sua nova cidade: ")
            
            #endereco
            case 4:
                self.__endereco = input("Digite seu novo endereco: ")
            
            #telefone
            case 5:
                self.__telefone = input("Digite seu novo telefone: ")
            
            #cpf
            case 6:
                self.__cpf = input("Digite seu novo cpf: ")
            
            #rg
            case 7:
                self.__rg = input("Digite seu novo rg: ")
            
            #usuario
            case 8:
                self.__usuario = input("Digite seu novo usuario: ")
            
            #senha
            case 9:
                self.trocarSenha(input("Digite sua nova senha: "))
        def 

class Funcionario(Pessoa):
    def __init__(self, cargo, cargaHoraria):
        self.__cargo = input("Digite qual o seu cargo: ")
        self.__cargaHoraria = int(input("Digite sua carga horária em horas: "))

    def cadastrarDep(self):
        pass

    def cadastrarPis(self):
        pass        
