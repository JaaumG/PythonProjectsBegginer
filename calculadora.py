#calculadora
print("olá seja bem vindo a calculadora")
conta = input("que tipo de conta voce deseja fazer ?\n multiplicacao, divisao, soma ou subtracao?\n")
if conta == "multiplicacao":
    var1 = input("digite o primeiro valor que voce desja multiplicar\n")
    var1 = float(var1)
    var2 = input("digite o segundo valor que voce desja multiplicar\n")
    var2 = float(var2)
    print(f'{"resultado = "}{var1*var2}')
elif conta == "divisao":
    var1 = input("digite o primeiro valor que voce desja dividir\n")
    var1 = float(var1)
    var2 = input("digite o segundo valor que voce desja dividir\n")
    var2 = float(var2)
    print(f'{"resultado = "}{var1/var2}')    
elif conta == "soma":
    var1 = input("digite o primeiro valor que voce desja somar\n")
    var1 = float(var1)
    var2 = input("digite o segundo valor que voce desja somar\n")
    var2 = float(var2)
    print(f'{"resultado = "}{var1+var2}')        
elif conta == "subtracao":
    var1 = input("digite o primeiro valor que voce desja subtrair\n")
    var1 = float(var1)
    var2 = input("digite o segundo valor que voce desja subtrair\n")
    var2 = float(var2)
    print(f'{"resultado = "}{var1-var2}')