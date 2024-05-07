# Exercício 11

# Crie um programa em Python para controle de estoque de produtos de um estabelecimento
# que vende produtos de hortifrúti. Para o estoque, armazene tudo dentro de um dicionário
# contendo listas. A chave deverá ser o nome de cada produto e dentro de cada lista
# teremos o preço e a quantidade disponível no estoque. O estoque pode estar
# pré-cadastrado no sistema com quantos itens desejar.

# Simule uma compra. Peça ao usuário para digitar o nome do produto e a quantidade que
# deseja até que ele decida encerrar a compra. Ao final, apresente tudo na tela em um
# formato organizado, mostrando o total a ser pago por produto e o total final do pedido.

# Ainda, dê baixa no sistema descontado o que foi comprado do total. Imprima na tela o estoque restante.

estoque_hortifruti = {
    'tomate': [0.39, 100],
    'alface': [2.88, 25],
    'batata': [0.49, 80],
    'cenoura': [0.22, 100],
    'maça': [0.79, 60],
    'banana': [5, 12]
}

def valida_op(pergunta):
    op = input(pergunta).lower()
    while(op not in estoque_hortifruti.keys()):
        print('Digite uma opção valida\n')
        op = input(pergunta).lower()
    return op

def valida_int(pergunta, produto):
    x = int(input(pergunta))
    min = 1
    max = produto[0]
    while((x < min) or (x > max)):
        print(f'Quantidade invalida, temos um estoque de {max} da/o {produto[1]}.')
        x = int(input(pergunta))
    return x

def nova_compra(total):
    pergunta = input('Continuar comprando? (S/N) ')
    if (pergunta in 'Ss'):
        return compra_hortifruti(total)
    elif (pergunta in 'Nn'):
        print(f'\n--- Para controle interno ---\nEstoque atualizado após compra:\n{estoque_hortifruti}\n\n')
        return print(f'Total a pagar: R$ {total}')
    else:
        print('Opção inválida')
        return nova_compra(total)

def compra_hortifruti(total=0):
    print('\n' + '-' * 3 + 'Lista de Itens' + '-' * 3)
    i = 1
    for keys, values in estoque_hortifruti.items():
        print(f'\n {i} - Item: {keys[0].upper()+keys[1:]} - Valor: R$ {values[0]}')
        i += 1
    print('\n' + '-' * 3 + 'Fim da lista' + '-' * 3 + '\n')
    op_produto = valida_op('Qual item gostaria de comprar? ')
    produto = [estoque_hortifruti.get(op_produto)[1], op_produto]
    op_quantidade = valida_int('Quantas unidades gostaria de comprar desse produto? ', produto)
    total_compra = op_quantidade * estoque_hortifruti.get(op_produto)[0]
    print(f'\nVocê escolheu {op_quantidade} unidades de {op_produto}.\nTotal: R$ {round(total_compra,2)}\n')
    estoque_hortifruti.get(op_produto)[1] -= op_quantidade
    total += total_compra
    return nova_compra(total)

while True:
    compra = input('Gostaria de iniciar uma compra? (S/N) ')

    if (compra in 'Ss'):
        compra_hortifruti()
        break
    elif (compra in 'Nn'):
        print('Retorne assim que precisa de uma fruta ou legume!')
        break
    else:
        print('Opção invalida, aperte S para Sim e N para Não!')
        continue
