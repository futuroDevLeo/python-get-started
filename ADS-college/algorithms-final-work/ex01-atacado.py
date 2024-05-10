# QUESTÃO 1 de 4

# Imagina-se que você é um dos programadores responsáveis pela construção de app de vendas
# para uma determinada empresa X que vende em atacado. Uma das estratégias de vendas dessa
# empresa X é dar desconto maior conforme o valor da compra, conforme a listagem abaixo:

# •	Se valor for menor que 2500 o desconto será de 0%;
# •	Se valor for igual ou maior que 2500 e menor que 6000 o desconto será de 4%;
# •	Se valor for igual ou maior que 6000 e menor que 10000 o desconto será de 7%;
# •	Se valor for igual ou maior que 10000 o desconto será de 11%;

# Elabore um programa em Python que:
# A. Deve-se implementar o print com uma mensagem de boas-vindas que apareça o seu nome; OK
# B. Deve-se implementar o input do valor unitário e da quantidade do produto; OK
# C. Deve-se implementar o desconto conforme a enunciado acima
#   (obs.: atente-se as condições de menor, igual e maior); OK
# D. Deve-se implementar o valor total sem desconto e o valor total com desconto; OK
# E. Deve-se implementar as estruturas if, elif e else (todas elas); OK
# F. Deve-se inserir comentários relevantes no código; OK
# G. Deve-se apresentar na saída de console uma mensagem de boas-vindas com seu nome; OK
# H. Deve-se apresentar na saída de console um pedido recebendo desconto
#   (valor total sem desconto maior ou igual a 2500); OK


print('Bem-vindo a Loja do Leonardo Nunes')

# Coleta do usuário o valor unitário do produto e a quantidade comprada
valor = int(input('Entre com o valor do produto: '))
qtd_produto = int(input('Entre com a quantidade do produto: '))

# Calcula o valor total da compra multiplicando o valor do produto pela quantidade de produtos
valor_compra = valor * qtd_produto

# Verifica se o valor total da compra é maior ou igual a 10000
if (valor_compra >= 10000):
    # Se o valor total da compra for maior ou igual a 10000, o comprador recebe 11% de desconto
    desconto = valor_compra*0.11
elif (valor_compra >= 6000):
    # Se o valor total da compra for maior ou igual a 6000, o comprador recebe 7% de desconto
    desconto = valor_compra*0.07
elif (valor_compra >= 2500):
    # Se o valor total da compra for maior ou igual a 2500, o comprador recebe 4% de desconto
    desconto = valor_compra*0.04
else:
    # Se o valor total da compra for inferior a 2500, o comprador não recebe desconto
    desconto = 0

# Calcula o valor final da compra aplicando o desconto
total = valor_compra - desconto

# Informa o valor SEM e COM desconto
print(f'O valor SEM desconto: R$ {valor_compra:.2f}')
print(f'O valor COM desconto: R$ {total:.2f}')