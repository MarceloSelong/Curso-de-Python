#Escreva um programa que pergunte o salário de um funcionário
#E calcule o valor do seu aumento.
#Para salário superiores a R$1.250,00, calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%.

sal = int(input('Informe o valor do seu sálario: '))
if sal >= 1250:
    print('Seu novo salário será de R${:.0f}.'.format((sal/100*10)+sal))
else:
    print('Seu novo salário será de R${:.0f}.'.format((sal/100*15)+sal))
