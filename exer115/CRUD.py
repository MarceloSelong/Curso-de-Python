# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de
# texto simples.
# O sistema só vai ter duas opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
from __init__ import menu, criar_arquivo, verificar_arquivo, escolha #importa as bibliotecas utilizadas
criar_arquivo() #chama a função criar_arquivo
if verificar_arquivo(): #verificação de existência de arquivo
    print('Arquivo em branco.')
    menu() #abertura do menu de escolha
    escolha() #escolha do usuário
else:
    menu()
    escolha()






