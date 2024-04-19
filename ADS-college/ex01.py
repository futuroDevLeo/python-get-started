def calculo_de_desconto(preco, percentual):
    desconto = preco * (percentual/100)
    res = preco - desconto
    return f'O preço do produto com desconto é: {round(res, 2)}'

input1 = float(input('Digite o preço do produto: '))
input2 = float(input('Digite o percentual de desconto a ser aplicado: '))

print(f'O valor do produto é {input1}. Desconto de {input2}%')
print(calculo_de_desconto(input1, input2))