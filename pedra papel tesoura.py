#pedra papel tesoura
import random
import time
menu = input("deseja jogar pedra papel tesoura ?\n")
if menu == "sim":
    print("ok! se prepare")
    escolha = input("digite sua jogada, prometo nao vou trapacear, hihi\n")
    escolha = str(escolha)
    if escolha == "pedra":
        escolha = 1
    elif escolha == "papel":
        escolha = 2
    elif escolha == "tesoura":
        escolha = 3
    computador = random.randrange(1, 4)
    computador = int(computador)
    if computador == 1:
        print("pedra, papel tesoura...")
        time.sleep(2)
        if computador == escolha:
            print("Empate")
        elif escolha == 2:
            print("joguei pedra e voce ganhou!")
        elif escolha == 3:
            print("joguei pedra e voce perdeu!")
    elif computador == 2:
        print("pedra, papel tesoura...")
        time.sleep(2)
        if computador == escolha:
            print("Empate")
        elif escolha == 1:
            print("joguei papel e voce perdeu!")
        elif escolha == 3:
            print("joguei papel e voce ganhou!")
    elif computador == 3:
        print("pedra, papel tesoura...")
        time.sleep(2)
        if computador == escolha:
            print("Empate")
        elif escolha == 1:
            print("joguei tesoura e voce ganhou!")
        elif escolha == 2:
            print("joguei tesoura e voce perdeu!")

	