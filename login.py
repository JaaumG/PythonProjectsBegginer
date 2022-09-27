#sistema de login e senha
import time
print("inicializando...")
time.sleep(2)
print("inicializado")
time.sleep(1)
opcao1 = input("criar ou logar ?\n")
if opcao1 == "criar":
    login = input("digite seu login \n")
    login = str(login)
    registro = open("login.txt", "a")
    registro.writelines(login)
    registro.close()
    senha = input("digite aqui sua senha \n")
    senha = str(senha)
    registro = open("senha.txt", "a")
    registro.writelines(senha)
    registro.close()
    print("login e senha salvos")
elif opcao1 == "logar":
    login = input("digite seu login\n")
    login = str(login)
    registro = open("login.txt", "r")
    registro = registro.read()
    registro = str(registro)
    if login == registro:
        senha = input("digite aqui sua senha\n")
        senha = str(senha)
        registro = open("senha.txt", "r")
        registro = registro.read()
        registro = str(registro)
        if senha == registro:
            print("seja bem vindo")
        else:
            print("senha incorreta")
    else:
        print("login incorreto tente novamente")