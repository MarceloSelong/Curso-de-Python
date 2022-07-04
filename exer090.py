# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final mostre o conteúdo da estrutura na tela.
# Média 7 ou mais = aprovado, menos que isso = reprovado.
alunos = dict()
alunos['nome'] = str(input('Informe o nome do aluno: '))
alunos['media'] = float(input('Informe a média desse aluno: '))
if alunos['media'] >= 7:
    alunos['situação'] = 'Aprovado'
else:
    alunos['situação'] = 'Reprovado'
print('=-'*30)
print(f'O nome do aluno é {alunos["nome"]}')
print(f'A média do aluno é {alunos["media"]}')
print(f'A situação desse aluno é: {alunos["situação"]}')
 