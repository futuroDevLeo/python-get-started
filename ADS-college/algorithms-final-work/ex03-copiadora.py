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

# Elabore um programa em Python que: 
 
# A. Deve-se implementar o print com uma mensagem de boas-vindas que apareça o seu nome;
# B. Deve-se implementar a função escolha_servico() em que:
#   a. Pergunta o servico desejado;
#   b. Retorna o valor servico com base na escolha do usuário;
#   c. Repete a pergunta do item B.a se digitar uma opção diferente de: dig/ico/ipb/fot;
# C. Deve-se implementar a função num_pagina() em que:
#   a. Pergunta o número de páginas;
#   b. Retorna o número de páginas com desconto seguindo a regra do enunciado
#       (desconto calculado em cima do número de páginas);
#   c. Repete a pergunta do item C.a se digitar um valor acima de 20000 ou valor não
#       numérico (use try/except para não numérico)
# D. Deve-se implementar a função servico_extra() em que:
#   a. Pergunta pelo serviço adicional;
#   b. Retornar o valor de apenas uma das opções de adicional 
#   c. Repetir a pergunta item D.a se digitar uma opção diferente de: 1/2/0;
# E. Deve-se implementar o total a pagar no código principal (main), ou seja, não pode estar
#   dentro de função, conforme o enunciado;
# F. Deve-se implementar try/except;
# G. Deve-se inserir comentários relevantes no código;
# H. Deve-se apresentar na saída de console uma mensagem de boas-vindas com o seu nome;
# I. Deve-se apresentar na saída de console um pedido no qual o usuário errou a opção de
#   serviço;
# J. Deve-se apresentar na saída de console um pedido no qual o usuário digitou ultrapassou
#   no número de páginas;
# K. Deve-se apresentar na saída de console um pedido com opção de serviço, número de páginas
#   e serviço extra válidos;
