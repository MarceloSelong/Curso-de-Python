#Crie um programa que leia vários número inteiros pelo teclado.
#O programa só vai parar quando o usuário digitar o valor 1, que é a condição de parada.
#No final, mostre quantos números foram digitados e qual foi a soma entre eles.(Desconsiderando o flag(999)).
repeteco = 1
contador = 0
soma = 0
num = 0
print('\033[33mSoma dos valores digitados:\033[m ')
while repeteco == 1:
    num = int(input('Informe um valor: '))
    contador += 1
    soma += num
    repeteco = int(input("""Deseja continuar ?
    (1) para sim
    (0) para não. """))
    while repeteco != 0 and repeteco != 1:
        repeteco = int(input('Informe corretamente: '))
print('A soma entre os {} valores digitados foi {}.'.format(contador, soma))
print('Fim')