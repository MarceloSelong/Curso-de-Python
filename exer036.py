#Escreva um programa para aprovar um emprésimo bancário para a compra de uma casa.
#O programa vai perguntar o valor da casa,
#o salário do comprador,
#e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal,
#Sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
print('Simulador de empréstimo para compra de imóvel')
valor = int(input('Informe o valor do imóvel: '))
sal = int(input('Informe o seu salário: '))
anos = int(input('Em quantos anos quer pagar o imóvel ? '))
prestacao = valor/(anos*12)
print()
print('O valor que deve ser pago por mês é de R${:.0f}'.format(prestacao))
if prestacao >= (sal*30)/100:
    print('A prestação da compra do imóvel é maior que 30% do seu salário.')
    print('\033[31mEMPRÉSTIMO NEGADO!!!\033[m')
else:
    print('\033[34mEMPRÉSTIMO APROVADO!!!\033[m')
print('Fim')
