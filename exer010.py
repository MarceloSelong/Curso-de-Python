print('Conversor para dólar')
d = int(input('Quanto dinheiro você tem ? '))
print('Você pode comprar {}U${:.3f}{}.'.format('\033[4;34m', d/4.78, '\033[m'))
