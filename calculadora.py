print("------Tabuada Virtual------")
while True:
    escolha1 = int(input("Escolha um número: "))
    escolha2 = int(input("Escolha outro número: "))
    print("Escolha uma operação: \n 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n 5 - Sair do Programa.")
    operacao = int(input("Operação escolhida: "))
    if operacao == 1:
        soma = escolha1 + escolha2
        print(f"A soma entre {escolha1} e {escolha2} é igual a {soma}")
    elif operacao == 2:
        subtracao = escolha1 - escolha2
        print(f"A subtração de {escolha1} e {escolha2} é igual a {subtracao}")
    elif operacao == 3:
        multiplicacao = escolha1 * escolha2
        print(f"A multiplicação de {escolha1} e {escolha2} é igual a {multiplicacao}")
    elif operacao == 4:
        divisao = escolha1 / escolha2
        print(f"A divisão de {escolha1} e {escolha2} é igual a {divisao}")
    else:
        break
