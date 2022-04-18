# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens até 200km.
# E R$0,45 para viagens mais longas.
km = int(input('Informe a distância em Km da viagem.'))
if km <=200:
     print('O valor da passagem será de: R${:.0f}.'.format(km*0.5))
else:
    print('O valor da passagem será de: R${:.0f}.'.format(km*0.45))
