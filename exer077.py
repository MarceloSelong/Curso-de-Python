# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# depois disso, mostrar, para cada palavras quais são as suas vogais.

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
            'mercado', 'programador', 'futuro')
for c in range(0, len(palavras)):
    print(f'Na palavra {palavras[c].upper():.<12} temos: {palavras[c].count("a")*"a "}{palavras[c].count("e")*"e "}'
          f'{palavras[c].count("i")*"i "}{palavras[c].count("o")*"o "}{palavras[c].count("u")*"u "}')
