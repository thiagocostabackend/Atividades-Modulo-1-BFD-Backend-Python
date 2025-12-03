#6. Peça a idade e, se for maior de idade, pergunte se tem habilitação (sim/não) e diga se pode dirigir.

idade = int(input("Digite a sua idade: "))
if idade > 18:
    habilitacao = input("Você é maior de idade. Possui habilitação? (sim/não): ").strip().lower()
    if habilitacao == "sim":
        print("Você pode dirigir.")
    else:
        print("Você não pode dirigir.")