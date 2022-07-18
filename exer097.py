# Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
# Ex: Escreva('Olá, mundo!')

# Saída:
# ----------------
# Olá, mundo !
# ----------------

def escreva(txt):
    tamanho = len(txt)+3
    print('='*(3+len(txt)))
    print(f'{txt:^{tamanho}}')
    print('='*(3+len(txt)))


escreva(str(input('Escreva uma mensagem personalizada: ')))

