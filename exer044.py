#Elabore um programa que calcule o valor a ser pago por um produto,
#considerando seu preço normal e a condição de pagamento.
#-À vista dinheiro/cheque: 10% de desconto
#-À vista no cartão: 5% de desconto
#Em até 2x no cartão: preço normal
#Em 3x ou mais no cartão: 20% de juros.
print('Atacadão da Moda')
preco = str(input('Informe o preço do produto: '))
preco = preco.replace(',', '.')
preco = float(preco)
print('Informe a condição de pagamento: ')
print('(1) para dinheiro ou cheque.')
print('(2) nó débito.')
print('(3) em até duas vezes no crédito')
print('(4) em 3x ou mais no crédito')
cond = int(input())
if cond == 1:
    print('O valor a ser pago pelo produto com 10% de desconto é: \033[31mR${:.2f}\033[m.'.format(preco-(preco*10)/100))
elif cond == 2:
    print('O valor a ser pago pelo produto com 5% de desconto é: \033[31mR${:.2f}\033[m.'.format(preco-(preco*5)/100))
elif cond == 3:
    print('O valor a ser pago pelo produto é: \033[31mR${:.2f}\033[m.'.format(preco))
elif cond == 4:
    print('O valor a ser pago pelo produto com 20% de acréscimo é: \033[31mR${:.2f}\033[m.'.format((preco*20)/100+preco))
