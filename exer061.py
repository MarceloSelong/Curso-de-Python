# Refaça o desafio 51, lendo o primeiro termo e a razão de uma P.A.,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.
from time import sleep

repetir = 1
opdaconstante = 0
while repetir == 1:
    primeirotermo = int(input('Informe o primeiro termo: '))
    razão = int(input('Informe a razão desta P.A.: '))
    x = primeirotermo + (10 - 1) * razão
    print()
    # ----------------------------Constante------------------------------------#
    if razão == 0:
        contador = 0
        print('Esta é uma P.A. \033[31mconstante\033[m.')
        # ------------------------Visual da P.A.-------------------------------#
        while contador < 10:
            if contador != 9:
                print('{}, '.format(primeirotermo), end='')
                contador += 1
            else:
                print('{}.'.format(primeirotermo))
                contador += 1
        # ------------------------Menu de escolha------------------------------#
        print()
        opdaconstante = int(input("""Gostaria de começar novamente?
[1] para sim.
[0] para não: """))
        if opdaconstante == 0:
            print('\033[31mEncerrando...\033[m')
            repetir = 0
            sleep(2)
        elif opdaconstante == 1:
            print('\033[31mReiniciando...\033[m')
            repetir = 1
            sleep(2)
            print("\n" * 130)
        else:
            while opdaconstante != 0 and opdaconstante != 1:
                opdaconstante = int(input('Informe corretamente:'))
                if opdaconstante == 0:
                    print('\033[31mEncerrando...\033[m')
                    repetir = 0
                    opdaconstante = 0
                    sleep(2)
                elif opdaconstante == 1:
                    print('\033[31mReiniciando...\033[m')
                    repetir = 1
                    opdaconstante = 1
                    sleep(2)
                    print("\n" * 130)
    # -------------------------------Crescente------------------------------#
    elif razão > 0:
        print('Esta é uma P.A. \033[31mcrescente\033[m.')
        contador = primeirotermo
        while contador < x + 1:
            if contador < x:
                print('{}, '.format(contador), end='')
                contador += razão
            else:
                print('{}.'.format(contador))
                contador += razão
        print()
        repetir = int(input("""Gostaria de repetir?
[1] para sim.
[0] para não: """))
        if repetir == 0:
            print('\033[31mENCERRANDO...\033[m')
            sleep(2)
        elif repetir == 1:
            print('\033[31mReiniciando...\033[m')
            sleep(2)
            print('\n' * 130)
        else:
            while repetir != 0 and repetir != 1:
                repetir = int(input('Informe corretamente:'))
            if repetir == 1:
                print('\033[31mReiniciando...\033[m')
                sleep(2)
                print('\n' * 130)
            elif repetir == 0:
                print('\033[31mEncerrando...\033[m')
                sleep(2)
    # ------------------------------Decrescente-----------------------------#
    elif razão < 0:
        print('Esta é uma P.A. \033[31mdecrescente\033[m.')
        contador = primeirotermo
        while contador > x - 1:
            if contador > x:
                print('{}, '.format(contador), end='')
                contador += razão
            else:
                print('{}.'.format(contador))
                contador += razão
        print()
        repetir = int(input("""Gostaria de repetir?
[1] para sim.
[0] para não: """))
        if repetir == 0:
            print('\033[31mENCERRANDO...\033[m')
            sleep(2)
        elif repetir == 1:
            print('\033[31mReiniciando...\33[m')
            sleep(2)
            print('\n' * 130)
        else:
            while repetir != 0 and repetir != 1:
                repetir = int(input('Informe corretamente: '))
                if repetir == 0:
                    print('\033[31mENCERRANDO...\033[m')
                    sleep(2)
                elif repetir == 1:
                    print('\033[31mReiniciando...\33[m')
                    sleep(2)
                    print('\n' * 130)
