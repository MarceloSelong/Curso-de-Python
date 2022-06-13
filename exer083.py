# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu código deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
import re
expressão = input('Digite um expressão matemática: ')
expressão = re.sub('[0-9]', '', expressão)
expressão = re.sub('[a-z]', '', expressão)
expressão = re.sub('[/*+-.,]', '', expressão)
expressão = re.sub('[²³]', '', expressão)
expressão = re.sub('[A-Z]', '', expressão)
while '()' in expressão:
    expressão = expressão.replace('()', '')
if '(' in expressão or ')' in expressão:
    print('Expressão inválida')
if expressão == '':
    print('A expressão é válida')
