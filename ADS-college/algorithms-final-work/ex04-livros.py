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

# Elabore um programa em Python que:
 
# A. Deve-se implementar o print com uma mensagem de boas-vindas que apareça o seu nome;
# B. Deve-se implementar uma lista vazia com o nome de lista_livro e a variável id_global
#  com valor inicial igual a 0;
# C. Deve-se implementar uma função chamada cadastrar_livro(id) em que:
#   a. Pergunta nome, autor, editora do livro;
#   b. Armazena o id (este é fornecido via parâmetro da função), nome, autor, editora dentro
#    de um dicionário;
#   c. Copiar o dicionário para dentro da lista_livro;
# D. Deve-se implementar uma função chamada consultar_livro() em que:
#   a. Deve-se perguntar qual opção deseja
#     (1. Consultar Todos / 2. Consultar por Id / 3. Consultar por Autor / 4. Retornar ao menu):
#       i. Se Consultar Todos, apresentar todos os livros com todos os seus dados cadastrados;
#       ii. Se Consultar por Id, apresentar o livro específico com todos os seus dados cadastrados;
#       iii. Se Consultar por Autor, apresentar o(s) livro(s) do autor com todos os seus dados
#        cadastrados;
#       iv. Se Retornar ao menu, deve-se retornar ao menu principal;
#       v. Se Entrar com um valor diferente de 1, 2, 3 ou 4, printar "Opção inválida" e repetir
#        a pergunta D.a.
#       vi. Enquanto o usuário não escolher a opção 4, o menu consultar livros deve se repetir.
# E. Deve-se implementar uma função chamada remover_livro() em que:
#   a. Deve-se pergunta pelo id do livro a ser removido;
#   b. Remover o livro da lista_livro;
#   c. Se o id fornecido não for de um livro da lista, printar “Id inválido” e repetir a
#    pergunta E.a.
# F. Deve-se implementar uma estrutura de menu no código principal (main), ou seja, não pode
#  estar dentro de função, em que:
#   a. Deve-se pergunta qual opção deseja
#    (1. Cadastrar Livro / 2. Consultar Livro / 3. Remover Livro / 4. Encerrar Programa):
#       i. Se Cadastrar Livro, acrescentar em um id_ global e chamar a função
#        cadastrar_livro(id_ global);
#       ii. Se Consultar Livro, chamar função consultar_livro();
#       iii. Se Remover Livro, chamar função remover_livro();
#       iv. Se Encerrar Programa, sair do menu (e com isso acabar a execução do código);
#       v. Se Entrar com um valor diferente de 1, 2, 3 ou 4, printar “Opção inválida"
#        e repetir a pergunta F.a.
#       vi. Enquanto o usuário não escolher a opção 4, o menu deve se repetir.
# G. Deve-se implementar uma lista de dicionários (uma lista contento dicionários dentro);
# H. Deve-se inserir comentários relevantes no código;
# I. Deve-se apresentar na saída de console uma mensagem de boas-vindas com o seu nome;
# J. Deve-se apresentar na saída de console um cadastro de 3 livros (sendo 2 deles no mesmo autor);
# K. Deve-se apresentar na saída de console uma consulta de todos os livros;
# L. Deve-se apresentar na saída de console uma consulta por código (id) de um dos livros;
# M. Deve-se apresentar na saída de console uma consulta por autor em que 2 livros sejam do mesmo autor;
# N. Deve-se apresentar na saída de console uma remoção de um dos livros seguida de uma consulta de todos os livros;

