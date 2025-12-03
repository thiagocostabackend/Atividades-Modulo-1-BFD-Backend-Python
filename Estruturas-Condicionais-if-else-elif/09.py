#9.Peça três números e diga qual é o maior.

numeros = []
maior = None
for i in range(3):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)
    if maior is None or num > maior: #Aqui acontece a substituição do maior
        maior = num
print(f"O maior número digitado foi: {maior}")