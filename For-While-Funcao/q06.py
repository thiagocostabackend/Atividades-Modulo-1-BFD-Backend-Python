vogais = "aeiouAEIOU"
contador = 0
palavra = input("Digite uma palavra: ")
for letra in palavra:
    if letra in vogais:
        contador += 1
print(f"A plavra '{palavra}' tem {contador} vogais.")