maior = None
print("Pense em 5 números:")
for i in range(5):
    num = int(input(f"Digite o {i + 1}º número: "))
    if maior is None or num > maior:
        maior = num
print(f"O maior número digitado foi: {maior}")