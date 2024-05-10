# QUESTÃO 3 de 4

# Você foi contratado para desenvolver um sistema de cobrança de serviços de uma copiadora.
# Você ficou com a parte de desenvolver a interface com o funcionário.
# A copiadora opera da seguinte maneira:

# •	Serviço de Digitalização (DIG) o custo por página é de um real e dez centavos;
# •	Serviço de Impressão Colorida (ICO) o custo por página é de um real; 
# •	Serviço de Impressão Preto e Branco (IPB) o custo por página é de quarenta centavos; 
# •	Serviço de Fotocópia (FOT) o custo por página é de vinte centavos; 

# •	Se número de páginas for menor que 20 retornar o número de página sem desconto;
# •	Se número de páginas for igual ou maior que 20 e menor que 200 retornar o número de
# páginas com o desconto é de 15%;
# •	Se número de páginas for igual ou maior que 200 e menor que 2000 retornar o número
# de páginas com o desconto é de 20%;
# •	Se número de páginas for igual ou maior que 2000 e menor que 20000 retornar o número
# de páginas com o desconto é de 25%;
# •	Se número de páginas for maior ou igual à 20000 não é aceito pedidos nessa quantidade
# de páginas;

# ♦	Para o adicional de encadernação simples (1) é cobrado um valor extra de 15 reais;
# ♦	Para o adicional de encadernação de capa dura (2) é cobrado um valor extra de 40 reais;
# ♦	Para o adicional de não querer mais nada (0) é cobrado um valor extra de 0 reais;

# O valor final da conta é calculado da seguinte maneira:

# total = (servico * num_pagina) + extra

# ---------------------------------------Funções---------------------------------------

# Função que mostra os serviços ofertados pela empresa e solicita do usuário a escolha do
# serviço desejado. Retorna o valor do serviço para cálculos posteriores.
def escolha_servico():
    while True:
        servico = input('Entre com o tipo de serviço desejado\nDIG - Digitação\nICO - Impressão Colorida\nIPB - Impressão Preto e Branco\nFOT - Fotocópia\n>>').upper()

        if servico != 'DIG' and servico != 'ICO' and servico != 'IPB' and servico != 'FOT':
            print('Escolha inválida, entre com o tipo de serviço novamente')
            continue
        else:
            if servico == 'DIG':
                return 0.1
            elif servico == 'ICO':
                return 1
            elif servico == 'IPB':
                return 0.4
            elif servico == 'FOT':
                return 0.2

# Função que solicita o número de páginas para calcular o desconto caso ultrapasse as
# 20 páginas, até 20000, sendo este o limite. Retorna uma mensagem de erro caso ultrapassado.
# Retorna o número de páginas que não receberão desconto.
def num_pagina():
    while True:
        try:
            num_pag = int(input('Entre com o número de páginas: '))
            if num_pag >= 20000:
                print('Não aceitamos tantas páginas de uma vez.')
                print('Por favor, entre com o número de páginas novamente.\n')
                continue
            else:
                if num_pag >= 2000 and num_pag < 20000:
                    num_pag -= round(num_pag*0.25)
                elif num_pag >= 200:
                    num_pag -= round(num_pag*0.20)
                elif num_pag >= 20:
                    num_pag -= round(num_pag*0.15)
                else:
                    num_pag
                print()
                return num_pag
        except ValueError:
            print('Por favor, entre com um número de páginas valido.\n')
            continue

# Função que mostra os serviços extras aos clientes e solicita que informe o serviço
# extra caso desejado, ou 0 caso deseje encerrar o serviço.
def servico_extra():
    while True:
        try:
            op = int(input(('Deseja adicionar algum servico?\n1 - Encadernação Simples - R$ 15.00\n2 - Encadernação Capa Dura - R$ 40.00\n0 - Não Desejo mais nada\n>>')))
            if op != 0 and op != 1 and op != 2:
                print('Opção inválida!\n')
                continue
            else:
                if op == 0:
                    extra = 0
                if op == 1:
                    extra = 15
                if op == 2:
                    extra = 40
                print()
                return extra
        except:
            print('Digite uma opção válida.\n')
            continue

# ----------------------------------Programa Pincipal----------------------------------

# Programa principal que imprime a mensagem de boas-vindas, chama as outras funções,
# calcula o valor total do serviço e imprime na tela o resultado.
print('Bem vindo a Copiadora do Leonardo Nunes\n')

servico = escolha_servico() # Seleção do serviço principal

num_pag = num_pagina() # Seleção do número de páginas

extra = servico_extra() # Seleção de serviços extras, se houver

total = (servico*num_pag) + extra # Cálculo do custo total

print(f'Total: R$ {total:.2f} (serviço: {servico:.2f} * páginas: {num_pag} + extra: {extra:.2f})')