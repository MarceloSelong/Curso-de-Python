while True:
    num = int(input('Gostaria de ver a tabuada de qual número? '))
    print('-'*30)
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c} = {num*c}')
    print('-'*30)
print('\033[31mEncerrando...\033[m')
