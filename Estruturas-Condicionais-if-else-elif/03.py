#3. Peça uma nota (0 a 10) e informe: Aprovado (>= 7), Recuperação (5 a 6.9) ou Reprovado (< 5).

nota = float(input("Digite a nota do aluno: "))
if nota >= 7.0:
    print("Aprovado")
elif nota >= 5.0:    # Nota entre 5.0 e 6.9 , por ordem lógica o programa já sabe que é menor que 7.0
    print("Recuperação")
else:
    print("Reprovado")