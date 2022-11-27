def cadastro():
    arquivo = dict()

    def nome():
        while True:
            try:
                arquivo['nome'] = str(input('Informe o nome da pessoa a ser cadastrada: '))
                if all(c.isalpha() or c.isspace() for c in arquivo['nome']):
                    break
            except:
                print('Opção inválida, informe novamente: ')
                return nome()

    nome()

    def idade():
        while True:
            try:
                arquivo['idade'] = int(input('Idade: '))
                break
            except:
                print('Opção inválida, informe novamente: ')
                return idade()

    idade()
    return arquivo


def menu():
    print('-' * 63)
    print(f"{'Menu Principal':^63}".upper())
    print('-' * 63)
    print('\033[31m[1]\033[m para cadastrar uma nova pessoa')
    print('\033[31m[2]\033[m para listar as pessoas já cadastradas')
    print('\033[31m[3]\033[m para deletar o arquivo existente')
    print('\033[31m[4]\033[m para encerrar')
    print('-' * 63)


def criar_arquivo():
    """
    Verifica se o arquivo existe. Se não existir, cria um arquivo em branco.
    :return:
    """
    from os import path
    try:
        create_arquivo = 'exer115\texto.txt'
        if path.exists(create_arquivo) is False:
            open("texto.txt", "x")
            print('Novo criado com sucesso.')
    except:
        print('Arquivo já existe.')


def verificar_arquivo():
    from os import stat
    isempty = stat('texto.txt').st_size == 0
    return isempty


def escolha():
    from time import sleep
    from os import stat
    from os import remove
    while True:
        choice = int(input('Sua opção: '))
        while choice != 1 and choice != 2 and choice != 3 and choice != 4:
            choice = int(input('\n\033[31mEscolha inválida!\033[m\n'
                               'Digite:\n\033[31m[1]\033[m para cadastrar uma nova pessoa\n'
                               '\033[31m[2]\033[m para listar as pessoas já cadastradas\n'
                               '\033[31m[3]\033[m para deletar o arquivo\n'
                               '\033[31m[3]\033[m para deletar o arquivo\n'
                               '\033[31m[4]\033[m para encerrar: '))
        if choice == 1:
            if stat('texto.txt').st_size == 0:
                cadastrar = cadastro()
                nome = str(cadastrar['nome']) + ' ' + str(cadastrar['idade'])
                arquivo1 = open("texto.txt", "a", encoding="utf-8")
                arquivo1.write(nome)
                arquivo1.write(' anos.')
                arquivo1.close()
                print('Cadastro efetuado com sucesso.')
                menu()
            else:
                cadastrar = cadastro()
                nome = cadastrar['nome'] + ' ' + str(cadastrar['idade'])
                arquivo1 = open("texto.txt", "a", encoding="utf-8")
                arquivo1.write('\n')
                arquivo1.write(nome)
                arquivo1.write(' anos.')
                arquivo1.close()
                print('Cadastro efetuado com sucesso.')
                menu()
        elif choice == 2:
            print('As pessoas cadastradas são:')
            with open("texto.txt", "r", encoding="utf-8") as arquivo:
                print(arquivo.read())
                arquivo.close()
                print('-' * 63)
                menu()
        elif choice == 3:
            try:
                remove('texto.txt')
                print('Arquivo excluído com sucesso.')
            except:
                print('O arquivo não existe.')
            finally:
                criar_arquivo()
        elif choice == 4:
            print('Encerrando...')
            sleep(2)
            break
