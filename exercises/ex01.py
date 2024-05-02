import random

def gerar_valor_aleatorio(quantidade_de_vezes: int, intervalo: list[int, int]) -> float:
    contador = 0
    total = 0
    while contador <= quantidade_de_vezes:
        x = round(random.uniform(intervalo[0],intervalo[1]), 2)
        print(x)
        total += x
        contador += 1
    print(f"O valor total é: {round(total, 2)}")
    print(f"O valor médio é de: {round(total/quantidade_de_vezes, 2)}")

quantidade = int(input("Digite a quantidade de valores que o programa deve gerar: "))
intervalo_inicial = int(input("Digite o valor minimo que pode ser gerado: "))
intervalor_final = int(input("Digite o valor maximo que pode ser gerado: "))
gerar_valor_aleatorio(quantidade, [intervalo_inicial, intervalor_final])
