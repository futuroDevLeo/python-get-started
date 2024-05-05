# Exercício 7

# Escreva um algoritmo que leia números inteiros via teclado.
# Somente valores positivos devem ser aceitos pelo programa.
# Ao final da execução, informe a média dos valores digitados.
# Realize a implementação com as instruções break e continue,
# e trabalhe com operações lógicas Truthy e Falsey.
# Não esqueça de empregar também operadores especiais de atribuição.

soma = 0
qtd_num = 0

while True:
    x = int(input('Digite um número inteiro: '))
    if x < 0:
        print('Digite apenas valores positivos')
        continue
    if not x:
        break
    soma += x
    qtd_num += 1

media = soma/qtd_num
print(f'A média dos valores digitados é: {round(media, 2)}')
