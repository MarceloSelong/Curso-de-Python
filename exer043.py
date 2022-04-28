#Desenvola uma lógica que leia o peso e a altura de uma pessoa,
#calcule seu IMC e mostre seu status,
#de acordo com a tabela abaixo:
#-Abaixo de 18.5: Abaixo do Peso
#-Entre 18.5 e 25: Peso ideal
#-25 até 30: Sobrepeso
#-30 até 40: Obesidade
#-Acima de 40: Obesidade Mórbida
peso = str(input('Informe seu peso: '))
altura = str(input('Informe sua altura: '))
peso = peso.replace(',', '.')
altura = altura.replace(',', '.')
peso = float(peso)
altura = float(altura)
imc = peso/(altura * altura)
print('Seu IMC é \033[34m{:.2f}\033[m'.format(imc))
if imc <= 18.4:
    print('\033[34mVocê está abaixo do peso ideal.\033[m')
elif imc >= 18.5 and imc <= 25:
    print('\033[4:32mParabéns, você está no peso ideal.\033[m')
elif imc >= 25.1 and imc <= 30:
    print('\033[31mCuidado! Você está com Sobrepeso.\033[m')
elif 30.1 <= imc <= 40:
    print('\033[31mMuito cuidado! Você está com obesidade.\033[m')
elif imc >= 40.1:
    print('\033[4;31mVOCÊ CORRE RISCO DE VIDA!!! Está com obesidade mórbida\033[m')
