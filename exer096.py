# Faça um programa que tenha uma funçã ocahamda área(), que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.
def área(largura, comprimento):
    total = largura * comprimento
    print(f'A área do terreno de {largura}x{comprimento} é de {total}m².')


print('Controle de terrenos:\n' + '-='*10)

área(float(input('Informe a largura (m): ')), float(input('Informe o comprimento (m): ')))
