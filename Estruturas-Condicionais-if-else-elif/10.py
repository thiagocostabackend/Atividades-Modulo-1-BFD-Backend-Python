'''10.Peça usuário e senha. Se forem 'admin' e '1234', exiba 'Acesso permitido', caso contrário 'Acesso
negado'.'''

usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")

if usuario == "admin" and senha == "1234":
    print("Acesso permitido")
else:
    print("Acesso negado")