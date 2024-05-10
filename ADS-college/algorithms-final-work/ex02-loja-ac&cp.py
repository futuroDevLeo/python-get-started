# QUESTÃO 2 de 4

# Você e sua equipe de programadores foram contratados para desenvolver um app de vendas para
# uma loja que vende Açaí e Cupuaçu. Você ficou com a parte de desenvolver a interface do
# cliente para retirada do produto.
# A Loja possui seguinte relação:

# •	Tamanho P de Cupuaçu (CP) custa 9 reais e o Açaí (AC) custa 11 reais;
# •	Tamanho M de Cupuaçu (CP) custa 14 reais e o Açaí (AC) custa 16 reais;
# •	Tamanho G de Cupuaçu (CP) custa 18 reais e o Açaí (AC) custa 20 reais;
# Elabore um programa em Python que: 
 
# A. Deve-se implementar o print com uma mensagem de boas-vindas que apareça o seu nome; OK
# B. Deve-se implementar o input do sabor (CP/AC) e o print “Sabor inválido. Tente novamente" OK
#   se o usuário entra com valor diferente de CP e AC;
# C. Deve-se implementar o input do tamanho (P/M/G) e o print “Tamanho inválido. Tente novamente" OK
#   se o usuário com entra valor diferente de P, M ou G;
# D. Deve-se implementar if, elif e/ou else com cada uma das combinações de sabor e tamanho; OK
# E. Deve-se implementar um acumulador para somar os valores dos pedidos; OK
# F. Deve-se implementar o input com a pergunta: “Deseja pedir mais alguma coisa?”. OK
#   Se sim repetir a partir do item B, senão encerrar o programa executar o print do acumulador;
# G. Deve-se implementar as estruturas de while, break, continue (todas elas); OK
# H. Deve-se inserir comentários relevantes no código;
# I. Deve-se apresentar na saída de console uma mensagem de boas-vindas com o seu nome; OK
# J. Deve-se apresentar na saída de console um pedido em que o usuário errou o sabor;
# K. Deve-se apresentar na saída de console um pedido em que o usuário errou o tamanho;
# L. Deve-se apresentar na saída de console um pedido com duas opções sabores diferentes e com
#   tamanhos diferentes;

def algo_mais():
    while True:
        res = input('Deseja mais alguma coisa? (S/N) ').upper()
        print()
        if res == 'S' or res == 'N':
            return res
        else:
            print('Opção inválida, digite S para Sim e N para Não\n')
            continue

print()
print('Bem-vindo a Loja de Gelados do Leonardo Nunes')
# Printando na tela o cardápio com tamanhos, sabores e valores do Açaí e do Cupuaçu
print('-'*20 + 'Cardápio' + '-'*20)
print('-'*48)
print('-'*3 + '|  Tamanho  | Cupuaçu (CP) |  Açaí (AC)  |' + '-'*3)
print('-'*3 + '|     P     |   R$  9.00   |  R$ 11.00   |' + '-'*3)
print('-'*3 + '|     M     |   R$ 14.00   |  R$ 16.00   |' + '-'*3)
print('-'*3 + '|     G     |   R$ 18.00   |  R$ 20.00   |' + '-'*3)
print('-'*48)
print()

acumulador = 0

while True:
    sabor = input('Entre com o sabor desejado (CP/AC): ').upper()

    if sabor != 'AC' and sabor != 'CP':
        print('Sabor inválido. Tente novamente\n')
        continue
    else:    
        tamanho = input('Entre com o tamanho desejado (P/M/G): ').upper()

        if tamanho != 'P' and tamanho != 'M' and tamanho != 'G':
            print('Tamanho inválido. Tente novamente\n')
            continue

    if sabor == 'AC':
        sabor = 'Açaí'
    elif sabor == 'CP':
        sabor = 'Cupuaçu'

    total = 0
    if sabor == 'Açaí' and tamanho == 'P':
        total = 11
    elif sabor == 'Açaí' and tamanho == 'M':
        total = 16
    elif sabor == 'Açaí' and tamanho == 'G':
        total = 20
    elif sabor == 'Cupuaçu' and tamanho == 'P':
        total = 9
    elif sabor == 'Cupuaçu' and tamanho == 'M':
        total = 14
    elif sabor == 'Cupuaçu' and tamanho == 'G':
        total = 18
    
    print(f'Você pediu um {sabor} no tamanho {tamanho}: R$ {total:.2f}\n')

    res = algo_mais()

    if res == 'N':
        acumulador += total
        print(f'O valor total a ser pago: R$ {acumulador:.2f}')
        break
    else:
        acumulador += total
        continue


