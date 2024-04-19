# Execício 3

# Crie uma variável de string que receba uma frase qualquer. Crie uma
# segunda variável, agora contendo a metade da string digitada. Imprima
# na tela somente os dois últimos caracteres da segunda variável do
# tipo string.

frase = input('Digite uma frase: ')
tam = len(frase)
metade_da_frase = frase[0:int(tam/2)]
print(metade_da_frase[-2:])