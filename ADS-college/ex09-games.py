# Exercício 9

# Suponha que você é um colecionador de jogos de videogame. Escreva um
# algoritmo que permita cadastrar esses jogos informando o nome e a qual
# videogame ele percente. Para isso, crie um menu de opções contendo:

# - Cadastrar novo item;
# - Listar tudo que foi cadastrado;
# - Sair.

def valida_op(pergunta, min, max):
    x = int(input(pergunta))
    while((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def existe_arquivo(nome_arquivo):
    try:
        a = open(nome_arquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criar_arquivo(nome_arquivo):
    try:
        a = open(nome_arquivo, 'wt+')
        a.close()
    except:
        print('Erro na criação do arquivo.')
    else:
        print(f'Arquivo {nome_arquivo} criado com sucesso.')

def listar_arquivo(nome_arquivos):
    try:
        a = open(nome_arquivos, 'rt')
    except:
        print('Erro ao listar o arquivo.')
    else:
        print('\n')
        print('--------------------')
        print(a.read())
        print('--------------------')
        print('\n')
    finally:
        a.close()

def cadastrar_jogo(nome_arquivo, nome_jogo, nome_videogame):
    try:
        a = open(nome_arquivo, 'at')
    except:
        print('Erro ao abrir o arquivo')
    else:
        a.write(f'\nJogo: {nome_jogo}\nPlataforma: {nome_videogame}\n')
    finally:
        a.close()


arquivo = 'games.txt'
if existe_arquivo(arquivo):
    print("Arquivo localizado no computador.")
else:
    print('Arquivo inexistente.')
    criar_arquivo(arquivo)

while True:
    print("""    --- Menu ---
    1 - Cadastrar novo item;
    2 - Listar cadastros;
    3 - Sair"""
    )
    op = valida_op("Escolha a opção desejada: ", 1, 3)
    if op == 1:
        jogo = input('Nome do jogo: ')
        videogame = input('Nome do videogame: ')
        cadastrar_jogo(arquivo, jogo, videogame)
    elif op == 2:
        listar_arquivo(arquivo)
    elif op == 3:
        print(' ')
        break
