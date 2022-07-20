# Faça um programa que tenha função notas() que pode receber várias notas de alunos e vai retornar um dicionário
# com as seguintes informações :
# A) Quantidade de notas
# B) A maior nota
# C) A menor nota
# D) A média da turma
# E) A situação (opcional)
# Mencione também as docstrings da função

def notas(*num, sit=False):
    """
    -> Função para registro de notas de alunos. COm quantidade de notas, maior e menor nota,
    média da turma e situação da turma.
    :param num: desempacota diversas notas
    :param sit: se True retorna situação da turma
    :return: retonra o dicionário com as informações
    """
    dict = {}
    dict['quant'] = len(num)
    dict['maior'] = max(num)
    dict['menor'] = min(num)
    media = sum(num) / len(num)  # cálculo da média da turma
    if sit:  # situação da turma
        if media >= 8:
            print('Situação: Excelente')
        elif media >= 7:
            print('Situação: Boa')
        elif media >= 6:
            print('Situação: Média')
        elif media >= 5:
            print('Situação: Ruim')
        elif media < 5:
            print('Situação: Péssima')
        return dict


print(notas(9, 6, 7, 8, sit=True))
help(notas)