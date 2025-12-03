#5. Peça a cor do semáforo (verde, amarelo, vermelho) e exiba a ação correspondente.

cor_semaforo = input("Digite a cor do semáforo (vermelho, amarelo, verde): ").strip().lower()
if cor_semaforo == "vermelho":
    print("Pare!")
elif cor_semaforo == "amarelo":
    print("Atenção!")
elif cor_semaforo == "verde":
    print("Siga!")
else:
    print("Cor do semáforo inválida.")