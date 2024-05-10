# QUESTÃO 2 de 4

# Você e sua equipe de programadores foram contratados para desenvolver um app de vendas para
# uma loja que vende Açaí e Cupuaçu. Você ficou com a parte de desenvolver a interface do
# cliente para retirada do produto.
# A Loja possui seguinte relação:

# •	Tamanho P de Cupuaçu (CP) custa 9 reais e o Açaí (AC) custa 11 reais;
# •	Tamanho M de Cupuaçu (CP) custa 14 reais e o Açaí (AC) custa 16 reais;
# •	Tamanho G de Cupuaçu (CP) custa 18 reais e o Açaí (AC) custa 20 reais;

# --------------------------------PROGRAMA PRINCIPAL---------------------------------------

# Função que pergunta ao usuário se ele quer algo mais e coleta a respostas
# caso seja 'S' ou 'N'. Caso algo diferente seja digitado, o programa exibe
# uma mensagem de erro e prende em um loop até que uma opção válida seja digitada.
def algo_mais():
    while True:
        res = input('Deseja mais alguma coisa? (S/N) ').upper()
        print()
        if res == 'S' or res == 'N':
            return res
        else:
            print('Opção inválida, digite S para Sim e N para Não\n')
            continue

# Printando na tela a mensagem de boas-vindas e o cardápio com tamanhos,
# sabores e valores do Açaí e do Cupuaçu.
print()
print('Bem-vindo a Loja de Gelados do Leonardo Nunes')
print('-'*20 + 'Cardápio' + '-'*20)
print('-'*48)
print('-'*3 + '|  Tamanho  | Cupuaçu (CP) |  Açaí (AC)  |' + '-'*3)
print('-'*3 + '|     P     |   R$  9.00   |  R$ 11.00   |' + '-'*3)
print('-'*3 + '|     M     |   R$ 14.00   |  R$ 16.00   |' + '-'*3)
print('-'*3 + '|     G     |   R$ 18.00   |  R$ 20.00   |' + '-'*3)
print('-'*48)
print()

# O acumulador do total da compra.
total = 0

# Loop que evita dados incorretos digitados pelo cliente durante o processo de compra.
while True:
    # Coleta do sabor do pedido, caso algo diferente de 'CP' ou 'AC' seja digitado entra
    # na condição if e retorna uma mensagem de erro e retorna para o início do loop.
    sabor = input('Entre com o sabor desejado (CP/AC): ').upper()
    if sabor != 'AC' and sabor != 'CP':
        print('Sabor inválido. Tente novamente\n')
        continue
    # Caso algum sabor válido seja digitado o programa entra na condição else e pede o
    # tamanho do produto. Uma nova condição if é aplicada caso um tamanho inválido seja
    # digitado e retorna para o início do loop.
    else:    
        tamanho = input('Entre com o tamanho desejado (P/M/G): ').upper()

        if tamanho != 'P' and tamanho != 'M' and tamanho != 'G':
            print('Tamanho inválido. Tente novamente\n')
            continue

    # Variável valor inicializada com '0' para posteriormente ser substituída pelo valor
    # do produto e tamanho escolhidos.
    # Cada condição if e elfi transforma a variável sabor no nome completo do sabor escolhido
    # e no valor do tamanho escolhido, para serem retornados posteriormente no programa.
    valor = 0
    if sabor == 'AC' and tamanho == 'P':
        sabor = 'Açaí'
        valor = 11
    elif sabor == 'AC' and tamanho == 'M':
        sabor = 'Açaí'
        valor = 16
    elif sabor == 'AC' and tamanho == 'G':
        sabor = 'Açaí'
        valor = 20
    elif sabor == 'CP' and tamanho == 'P':
        sabor = 'Cupuaçu'
        valor = 9
    elif sabor == 'CP' and tamanho == 'M':
        sabor = 'Cupuaçu'
        valor = 14
    elif sabor == 'CP' and tamanho == 'G':
        sabor = 'Cupuaçu'
        valor = 18
    
    # Retorna ao usuário o sabor escolhido, assim como o tamanho e o valor do produto.
    print(f'Você pediu um {sabor} no tamanho {tamanho}: R$ {valor:.2f}\n')

    # Chama a função, algo_mais e cria um loop aguardando uma resposta válida para continuar.
    res = algo_mais()

    # Recebe o retorno da função algo_mais caso válida e termina o loop caso 'N' seja escolhido,
    # imprimindo na tela o valor total do pedido acumulado na variável total fora do primeiro loop.
    if res == 'N':
        total += valor
        print(f'O valor total a ser pago: R$ {total:.2f}')
        break
    # Caso 'S' seja escolhido o programa cai no else, acumula o valor da compra atual no total e
    # reinicia o loop, assim o usuário pode comprar quantos produtos quiser e o total será acumulado
    # e retornado corretamente no final da compra.
    else:
        total += valor
        continue
