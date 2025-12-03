#1. Peça um número e diga se ele é positivo.
numero = float(input("Digite um número: "))
if numero > 0:
    print("O numero é positivo.")
elif numero<0:
    print("O número é negativo.")
else:
    print("O número é zero.")