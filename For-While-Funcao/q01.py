numeros = []
while True:
    num = float(input("Digite um número qualquer(ou '0' para sair): "))
    if num == 0:
        break
    numeros.append(num)
print(f"A soma dos números digitados é: {sum(numeros)}")