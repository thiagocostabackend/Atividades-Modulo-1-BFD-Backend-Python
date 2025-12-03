#8.Peça um número e diga se ele está entre 10 e 20 (inclusive).

num = int(input("Digite um número: "))
if num >= 10 and num <= 20:
    print("O número está entre 10 e 20.")
elif num < 10:
    print("O número é menor que 10.")
else:
    print("O número é maior que 20.")