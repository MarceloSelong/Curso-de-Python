# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = soma3 = maiseg = 0
#-----------------------------Alimentador da matriz e identificador de número par--------------------------------------#
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Informe um valor para a posição [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
#------------------------------------------Impressor da matriz---------------------------------------------------------#
print('\nO Resultado da matriz é:\n')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
#-----------------------------------Soma das valores da terceira coluna------------------------------------------------#
for l in range(0, 3):
    for c in range(2, 3):
        soma3 += matriz[l][c]
#--------------------------------------Maior valor da segunda coluna---------------------------------------------------#
for l in range(1, 2):
    for c in range(0, 3):
        if c == 0:
            maiseg = matriz[l][c]
        else:
            if matriz[l][c] > maiseg:
                maiseg = matriz[l][c]
#----------------------------------------------Resultado final---------------------------------------------------------#
print('-='*40)
print(f'A soma entre os pares digitados na matriz é: {soma}')
print('-='*40)
print(f'A soma entre os valores da terceira coluna é: {soma3}')
print('-='*40)
print(f'O maior valor da segunda linha é: {maiseg}')
