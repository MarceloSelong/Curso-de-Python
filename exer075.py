# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
tupla = (int(input('Informe um valor: ')), int(input('Informe um valor: ')), int(input('Informe um valor: ')),
         int(input('Informe um valor: ')),)
par = 0

print(f'O valor 9 apareceu {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O valor 3 apareceu na posição {tupla.index(3)+1}')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print(f'Os valores pares digitados foram:', end=' ')
for c in tupla:
    if c % 2 == 0:
        print(c, end=' ')
