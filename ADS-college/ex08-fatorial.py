# Exercício 8

# - Escreva uma função que calcule o fatorial de um número
# recebido como parâmetro e retorno o seu resultado.
# - Faça uma validação dos dados por meio de uma outra função,
# permitindo que somente valores positivos sejam aceitos.
# - Crie o help da sua função.

def valida_positivo(num):
    while num <= 0:
        num = int(input('Digite um valor inteiro para calculo da fatorial: '))
    return num

def calculo_fatorial(x):
    """
    Função que calcula a fatorial de um número inteiro fornecido como parametro!
    x: Valor que terá sua fatorial calculada;
    return: Mensagem exibindo o número escolhido e o resultado do calculo
        de sua fatorial
    """

    num = valida_positivo(x)

    fat = num-1
    soma = num
    
    if num == 1:
        return f"{num}! = {soma}"

    while fat > 1:
        soma *= fat
        fat -= 1
    return f"{num}! = {soma}"


x = int(input('Digite um valor inteiro para calculo da fatorial: '))
print(calculo_fatorial(x))