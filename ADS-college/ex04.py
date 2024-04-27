# Execício 4

# Uma empresa concedeu um bônus de 20% para todos seus funcionários com mais de cinco anos de empresa.
# Todos os outros que não se enquadram nesta categoria receberam uma bonificação de 10%, somente.
# Escreva um algoritmo que leia o salário do funcionário e seu tempo de empresa, e apresente a
# bonificação de cada funcionário na tela.

def calculo_de_bonificacao():
    nome_funcionario = input('Qual seu nome? ')
    salario_atual = float(input('Qual seu salário atual? '))
    ano_admissao = int(input('Em que ano em você entrou na empresa? '))
    ano_atual = 2024

    if (ano_admissao > ano_atual):
        print('O ano de admissão não pode ser superior ao ano atual!')
        return calculo_de_bonificacao()

    tempo_na_empresa = ano_atual - ano_admissao

    if (tempo_na_empresa >= 5):
        bonus = salario_atual * 0.2
        return print(f'{nome_funcionario}, sua bonificação é de {round(bonus)}, seu novo salario é: {round((salario_atual + bonus))}.')
    
    bonus = salario_atual * 0.1
    return print(f'{nome_funcionario}, sua bonificação é de {round(bonus)}, seu novo salario é: {round((salario_atual + bonus))}.')

calculo_de_bonificacao()