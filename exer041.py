#Crie um programa que leia a idade de um atleta e mostre sua categoria de acordo com a idade.
#-Até 9 anos: Mirim
#-Até 14 anos: Infantil
#-Até 19 anos: Junior
#-Até 20 anos: Sênior
#-Acima: Master
print('Categoria por idade')
idade = int(input('Informe a sua idade: '))
if idade <= 9:
    print('Você se enquadra na categoria: \033[34mMirim\033[m')
elif idade >= 10 and idade <= 13:
    print('Você se enquadra na categoria: \033[34mInfantil\033[m')
elif idade >= 14 and idade <= 18:
    print('Você se enquadra na categoria: \033[34mJúnior\033[m')
elif idade >= 19 and idade <= 20:
    print('Você se enquadra na categoria: \033[34mSênior\033[m')
elif idade >= 21:
    print('Você se enquadra na categoria: \033[34mMaster\033[m')
print('Fim')
