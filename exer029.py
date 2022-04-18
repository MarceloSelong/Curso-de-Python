#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80km/h.
#Mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por Km passado acima do limite.
vel = int(input('Informe a velocidade que passou no radar. '))
multa = (vel - 80)*7
if vel > 80:
    print('Você foi multado. A multa será no valor de: R${}.'.format(multa))
else:
    print('Você não foi multado.')
