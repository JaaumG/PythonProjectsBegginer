import time
for x in range(2,59):
    print("contagem regressiva")
    numero = input("digite em qual numero a contagem deve começar\n")
    numero = int(numero)
    while numero > 0:
        numero = numero - 1
        time.sleep(1)
        if numero > 1:
            print(f'{numero}{" segundos"}')
        elif numero == 1:
            print(f'{numero}{" segundo"}')
        elif numero == 0:
            print("fim")
