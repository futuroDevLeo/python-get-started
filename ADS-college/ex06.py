# Exercício 6

# Escreva um algoritmo que obtenha do usuário um valor inicial e um valor final.
# Para este intervalo especificado pelo usuário, calcule e mostre na tela:
# a. A quantidade de números inteiros e positivos;
# b. A quantidade de números pares;
# c. A quantidade de números impares;
# d. A respectiva média de cada um dos itens anteriores;
# Será necessário criar uma variável distinta para cada somatório, para cada
# quantidade e para cada média solicitada.

inicial = int(input('Informe um valor inicial. '))
final = int(input('Informe um valor final. '))
contador = inicial
inteiros = 0
pares = 0
impares = 0
soma_inteiros = 0
soma_pares = 0
soma_impares = 0

while (contador <= final):
    if (contador > 0):
        inteiros += 1
        soma_inteiros += contador
    
    if (contador % 2 == 0):
        pares += 1
        contador += 1
        soma_pares += contador
    else:
        impares += 1
        contador += 1
        soma_impares += contador
    
print(f'A quantidade de números inteiros e positivos é: {inteiros}')
print(f'A média de números inteiros e positivos é: {round(inteiros/soma_inteiros)}')
print(f'A quantidade de números pares é: {pares}')
print(f'A média de números inteiros e positivos é: {round(pares/soma_pares)}')
print(f'A quantidade de números impares é: {impares}')
print(f'A média de números inteiros e positivos é: {round(impares/soma_impares)}')
