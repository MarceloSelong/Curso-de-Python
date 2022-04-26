print('Liquidação 5% de desconto')
preco = float(input('Informe o preço do produto: '))
print('O novo preço deste produto será de: \033[4;31mR${:.2f}\033[m'.format(preco-preco/100*5))
