# Exercício 1

# Desenvolva um algoritmo que solicite ao usuário o preço de um produto
# e um percentual de desconto a ser aplicado a ele. Calcule e exiba o valor
# do desconto e preço final do produto.

def calculo_de_desconto(preco, percentual):
    desconto = preco * (percentual/100)
    res = preco - desconto
    return f'O preço do produto com desconto é: {round(res, 2)}'

input1 = float(input('Digite o preço do produto: '))
input2 = float(input('Digite o percentual de desconto a ser aplicado: '))

print(f'O valor do produto é {input1}. Desconto de {input2}%')
print(calculo_de_desconto(input1, input2))