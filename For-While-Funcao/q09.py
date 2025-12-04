def media(notas):
    soma = sum(notas)
    quantidade = len(notas)
    if quantidade == 0:
        return 0
    return soma / quantidade

print(media([10, 8, 9, 7, 6]))