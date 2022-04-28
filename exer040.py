#Crie um programa que leia duas notas de um aluno e calcule sua média,
#mostrando uma mensagem no final,
#de acordo com a média atingida.
#-Média abaixo de 5.0: REPROVADO
#-Média entre 5.0 e 6.9: RECUPERAÇÃO
#-Média 7.0 ou superior: APROVADO
print('Cálculo de média')
n1 = (input('Informe as suas duas médias: '))
n2 = (input())
n1 = n1.replace(',', '.')
n2 = n2.replace(',', '.')
n1 = float(n1)
n2 = float(n2)
soma = (n1+n2)/2
if soma < 5.0:
    print('Média {}. Você foi \033[031mREPROVADO!\033[m'.format(soma))
elif soma > 5.0 and soma < 6.9:
    print('Média {}. Você ficou em \033[33mRECUPERAÇÃO!\033[m'.format(soma))
elif soma > 7.0:
    print('Média {}. Você foi \033[34mAPROVADO!\033[m'.format(soma))
