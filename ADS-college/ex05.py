# Exercício 5

# Escreva um algoritmo em Python em que o usuário escolhe se ele quer comprar maçãs,
# laranjas ou bananas. Deverá ser apresentado na tela um menu com a opção 1 para maçã,
# 2 para laranja e 3 para banana. Após escolhida a fruta, deve-se digitar quantas
# unidades se quer comprar. O algoritmo deve calcular o preço total a pagar do produto
# escolhido e mostrá-lo na tela.


print('Escolha o que deseja comprar:')
print('1 - Maça')
print('2 - Laranja')
print('3 - Banana')

def hortifruti(total):
    preco_fruta1 = 2.3
    preco_fruta2 = 3.6
    preco_fruta3 = 1.85

    produto = int(input('Qual sua escolha? '))

    if (produto > 3 or produto < 1):
        print('Opção inválida')
        return hortifruti()
    
    qtd = int(input('Quantas unidades? '))

    def nova_compra():
        pergunta = input('Fazer nova compra? s/n ')
        if (pergunta == 's'):
            return hortifruti(total)
        elif (pergunta == 'n'):
            return print(f'Total: {total}')
        else:
            print('Opção inválida')
            return nova_compra()

    if (produto == 1):
        valor = qtd * preco_fruta1
        total = total + valor
        print(round(valor, 2))
        return nova_compra()
    elif (produto == 2):
        valor = qtd * preco_fruta2
        total = total + valor
        print(round(valor, 2))
        return nova_compra()
    elif (produto == 3):
        valor = qtd * preco_fruta3
        total = total + valor
        print(round(valor, 2))
        return nova_compra()


hortifruti(0)