# Exercício 2

# Escreva um programa que pergunte a quantidade de km percorridos
# por um carro alugado pelo usuário, assim como a quantidade de dias
# pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo
# que o carro custa R$ 60 por dia e R$ 0,15 por km rodado

def calculo_de_preco(km_rodados: int, qtd_de_dias: int) -> float:
    custo_por_dia = 60
    custo_por_km = 0.15

    valor_a_pagar = (km_rodados*custo_por_km) + (qtd_de_dias*custo_por_dia)
    return round(valor_a_pagar, 2)

km = int(input('Quantos km foram percorridos? '))
dias = int(input('Quantos dias o carro ficou alugado? '))

print(f'O valor a pagar é: {calculo_de_preco(km, dias)}')