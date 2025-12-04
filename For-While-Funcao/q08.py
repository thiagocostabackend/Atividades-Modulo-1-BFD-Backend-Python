def e_par(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
numero = int(input("Digite um número inteiro: "))
if e_par(numero):
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")