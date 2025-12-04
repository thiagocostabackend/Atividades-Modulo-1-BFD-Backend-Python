senha_correta = "python123"
while True:
    senha = input("Digite a senha: ").lower()
    if senha == senha_correta:
        print("Acesso permitido.")
        break
    else:
        print("senha incorreta. Tente novamente.")
