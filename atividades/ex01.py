import random

def gerar_valor_aleatorio(quantidade_de_vezes: int, intervalo: list[int, int]) -> float:
    contador = 0
    total = 0
    while contador <= quantidade_de_vezes:
        x = round(random.uniform(intervalo[0],intervalo[1]), 2)
        print(x)
        total += x
        contador += 1
    resultado = round(total, 2)
    print(f"O valor total é: {resultado}")
    print(f"O valor médio é de: {resultado/quantidade_de_vezes}")

gerar_valor_aleatorio(12, [0, 400])
