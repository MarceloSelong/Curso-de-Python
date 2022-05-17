# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa de verá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.
from time import sleep
maior = homens = mulmenor = 0
while True:
    print('-'*30)
    print('     CADASTRE UMA PESSOA       ')
    print('-'*30)
    idade = int(input('Idade:  '))
    sexo = input('Sexo [M/F]: ').upper()
    while sexo not in 'MF':
        sexo = input('\033[31mOpção incorreta!\033[m Pressione \033[33m"M"\033[m para masculino e '
                     '\033[33m"F"\033[m para feminino.').upper()
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F':
        if idade < 20:
            mulmenor += 1
    print('-'*30)
    continuar = input('   Quer continuar ? [S/N]').upper()
    while continuar not in 'SN':
        continuar = input('\033[31mOpção incorreta!\033[m Pressione \033[33m"S"\033[m para sim e '
                          '\033[33m"N"\033[m para não.').upper()
    if continuar == 'N':
        print('\n\033[31mEncerrando...\033[m')
        sleep(1)
        break
print(f"""\nTotal de pessoas com mais de 18 anos: {maior}
Ao todo temos {homens} homens cadastrados.
E temos {mulmenor} mulheres com menos de 20 anos.""")
