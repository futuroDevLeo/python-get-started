# QUESTÃO 4 de 4

# Você e sua equipe de programadores foram contratados por pequena empresa para desenvolver
# o software de gerenciamento de livros. Este software deve ter o seguinte menu e opções:

# 1) Cadastrar Livro
# 2) Consultar Livro
#     1. Consultar Todos 
#     2. Consultar por Id
#     3. Consultar por Autor
#     4. Retornar ao menu
# 3) Remover Livro
# 4) Encerrar Programa

# ----------------------------------------Funções-----------------------------------------

def cadastrar_livro(id):
    print('-'*40)
    print('-'*9 + ' MENU CADASTRAR LIVRO ' + '-'*9)
    print(f'Id do Livro: {id}')
    nome = input('Por favor entre com o nome do livro: ')
    autor = input('Por favor entre com o autor do livro: ')
    editora = input('Por favor entre com a editora do livro: ')
    print('-'*40)
    print()

    novo_livro = {
        'id': id,
        'nome': nome,
        'autor': autor,
        'editora': editora
    }

    lista_livro.append(novo_livro) # Adiciona o novo_livro ao final da lista_livro
    return

def consultar_livro():
    while True:
        print('-'*40)
        print('-'*9 + ' MENU CONSULTAR LIVRO ' + '-'*9)
        try:
            op = int(input('Escolha a opção desejada:\n1 - Consultar Todos os Livros\n2 - Consultar Livro por id\n3 - Consultar Livro(s) por autor\n4 - Retornar\n>>'))
            
            if op == 1:
                print('-'*10 + '\n')
                for i in range(0, len(lista_livro)): # Quebra a lista em pedaços e usa a variável i para retornar de uma em uma
                    id = lista_livro[i]['id'] # Pega o id de cada item da lista e coloca na váriavel local id
                    nome = lista_livro[i]['nome'] # Pega o nome de cada item da lista e coloca na váriavel local nome
                    autor = lista_livro[i]['autor'] # Pega o autor de cada item da lista e coloca na váriavel local autor
                    editora = lista_livro[i]['editora'] # Pega a editora de cada item da lista e coloca na váriavel local editora
                    print(f'id: {id}\nnome: {nome}\nautor: {autor}\neditora: {editora}\n') # Imprime na tela as informações de cada item da lista
                print('-'*10)
                continue
            if op == 2:
                id_detalhes = int(input('Digite o id do livro: '))
                if id_detalhes <= len(lista_livro): # Se o id informado for menor ou igual ao tamanho da lista_livro
                    print('-'*10 + '\n')
                    id = lista_livro[id_detalhes-1]['id'] # Pega apenas o id do livro escolhido
                    nome = lista_livro[id_detalhes-1]['nome'] # Pega apenas o nome do livro escolhido
                    autor = lista_livro[id_detalhes-1]['autor'] # Pega apenas o autor do livro escolhido
                    editora = lista_livro[id_detalhes-1]['editora'] # Pega apenas a editora do livro escolhido
                    print(f'id: {id}\nnome: {nome}\nautor: {autor}\neditora: {editora}\n') # Imprime na tela apenas os detalhes do livro confirme id foi escolhido
                    print('-'*10)
                    continue
                else:
                    print('\nOpção Inválida\n') # Caso o id escolhido seja inválido, ou seja, um número id que não existe destro da lista_livros imprime a mensagem de erro e reinicia o loop 
                    continue
            if op == 3:
                autor_livros = input('Digite o autor do(s) livro(s): ')
                autor_lista = [] # Declaração de uma lista vazia que será preenchida com os livros do autor definido
                for livro in lista_livro: # O laço de repetição procurará dentro de todo a lista os livros que tem o mesmo nome digitado e adicionará na lista autor_lista
                    if livro['autor'] == autor_livros:
                        autor_lista.append(livro)
                if len(autor_lista) > 0: # Se o tamanho da lista for maior que zero, quer dizer que algum livro do auto foi encontrado
                    print('-'*10 + '\n')
                    for i in range(0, len(autor_lista)): # Faz a desestruturação do dicionário e imprime na tela da mesma forma que nas outras opções
                        id = autor_lista[i]['id']
                        nome = autor_lista[i]['nome']
                        autor = autor_lista[i]['autor']
                        editora = autor_lista[i]['editora']
                        print(f'id: {id}\nnome: {nome}\nautor: {autor}\neditora: {editora}\n')
                    print('-'*10)
                else:
                    print('\nNão há livros cadastrados para o autor informado.\n') # Caso a lista esteja vazia a mensagem impressa na tela informará que não há livros desse autor
                continue
            if op == 4:
                break
            else:
                print('\nOpção Inválida\n') # Caso uma opção que não seja 1, 2, 3 ou 4 seja digitada, cairá no else e reiniciará o loop
                continue
        except ValueError:
            print('\nOpção Inválida\n') # Caso um valor não númerico seja digitado, cairá no expect e reiniciará o loop
            continue

def remover_livro():
    while True:
        print('-'*40)
        print('-'*10 + ' MENU REMOVER LIVRO ' + '-'*10)
        try:
            id = int(input('Digite o id do Livro a ser removido: '))
            count = 0
            index = 0
            for livro in lista_livro: # Esse laço vai percorrer a lista e procurar um id igual ao informado pelo usuario para exclusão
                if livro['id'] == id: # Se um id dentro da lista tiver o mesmo valor do id informado para exclusão
                    count += 1 # O contador será acrescido de 1
                    break
                index += 1 # Ao percorrer a lista o contador de index registrará o index que está sendo percorrido
            if count == 0: # Caso após o for o acumulador não tenha sido acrescido é porque o id informado não existe na lista
                print('Id inválido\n') # Imprime a mensagem de que o id informado não está na lista e reinicia o loop
                continue
            else: # Caso o contador tenha sido acrescido é porque o id informado está presente na lista, logo deve ser removido
                del lista_livro[index] # Remove o livro com o id infomado, mas que está no index ao qual ele foi encontrado, isso evita possíveis bugs caso um livro anteiro tenha sido removido
                print('Livro removido com sucesso!')
                break
        except ValueError:
            print('Digite um id válido.\n')
            continue

# -----------------------------------Programa Principal-----------------------------------

lista_livro = []
id_global = 0

print('Bem vindo a Livraria do Leonardo Nunes')

while True:
    print('-'*40)
    print('-'*12 + ' MENU PRINCIPAL ' + '-'*12)
    try:
        op = int(input('1 - Cadastrar Livro\n2 - Consultar Livro(s)\n3 - Remover Livro\n4- Sair\n>>'))

        if op == 1:
            id_global += 1
            cadastrar_livro(id_global)
            continue
        if op == 2:
            consultar_livro()
            continue
        if op == 3:
            remover_livro()
            continue
        if op == 4:
            break
        else:
            print('Opção inválida\n')
            continue
    except:
        print('Opção inválida\n')
        continue
