print('Carro alugado')
km = int(input('Informe a quantidade de Km rodados: '))
dias = int(input('Por quantos dias ele foi alugado? '))
print('O preço por dia é \033[35mR$60\033[m e o preço por km rodado é \033[35mR$0,45\033[m')
print('Logo, o valor a ser pago é de \033[4;31mR${:.2f}\033[m'.format(60*dias+km*0.15))