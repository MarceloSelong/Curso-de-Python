# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um dicionário,
# se por acaso a CTPS for diferente de zero(0), o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date
#---------------------------------------------------DATA---------------------------------------------------------------#
data_atual = date.today()
cadastro = dict()
#---------------------------------------------Programa principal-------------------------------------------------------#
cadastro = {'Nome': str(input('Informe o nome do funcionário: ')),
            'Ano de nascimento': int(input('Informe o ano de nascimento: ')),
            'Carteira de trabalho': int(input('Informe o número da carteira de trabalho. Pressione [0] se não ouver: '))
            }
cadastro.update({'Idade': int(data_atual.year - cadastro.get('Ano de nascimento'))})
if cadastro['Carteira de trabalho'] != 0:
    cadastro['Contratação'] = int(input('Informe o ano de contratação: '))
    cadastro['Salário'] = float(input('Informe o salário do funcionário: ').replace(',', '.'))
    cadastro.update({'Aposentadoria': 35 - (data_atual.year - cadastro.get('Contratação')) + cadastro.get('Idade')})
#----------------------------------------------------------------------------------------------------------------------#
#------------------------------------------Finalização do programa-----------------------------------------------------#
print()
for k, v in cadastro.items():
    print(f'{k}: {v}')
