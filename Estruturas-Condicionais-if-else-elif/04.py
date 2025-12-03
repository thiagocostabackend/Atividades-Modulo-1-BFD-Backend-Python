#4. Peça um número e verifique: se é positivo, se é par e se é múltiplo de 5.

numero = float(input("Digite um número: "))
if numero % 2 == 0:
    print("O número é par.")
    if numero % 5 == 0:
        print("O número também é múltiplo de 5.")
    else:
        print("O número não é múltiplo de 5.")
else:
    print("O número é ímpar.")