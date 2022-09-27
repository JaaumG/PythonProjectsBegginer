#jogar dados
import random
import time
dados = input("deseja jogar dados? sim/nao \n")
while dados == "sim":
    print("chacolhando o dado...\n")
    time.sleep(2)
    x = random.randrange(1, 7)
    print(f'{"o dado caiu em: "}{x}')
    dados = input("dejesa jogar novamente? sim/nao \n")    