"""
8. Faça um programa para uma calculadora simples com as seguintes operações: adição, subtração,
multiplicação e divisão.
O programa começa apresentando ao usuário um menu de opções semelhante ao mostrado abaixo:
Calculadora:
1 - Adição
2 - Subtração
3 - Multiplicação
4 - Divisão
5 - Sair do programa
Selecione sua opção:
Crie uma função chamada Menu, que exiba o menu acima e retorna a opção do usuário para o
programa principal. Se a opção for inválida, informe ao usuário e peça a ele para entrar com uma
opção válida.
De acordo com a opção do usuário, chame uma das seguintes funções: adicao, subtracao,
multiplicacao, divisao, passando como parâmetros dois números também informados pelo usuário.
Após a execução da operação o programa volta a apresentar o menu inicial até que o usuário encerre
o programa com a opção 5
"""


def menu():
    print('--' * 12)
    print('1 - Adição\n'
          '2 - Subtração\n'
          '3 - Multiplicação\n'
          '4 - Divisão\n'
          '5 - Sair do programa\n')
    print('--' * 12)


def soma(n1, n2):
    s = n1 + n2
    print(f'{n1} + {n2} = {s}')


def subtracao(n1, n2):
    s = n1 - n2
    print(f'{n1} - {n2} = {s}')


def multiplicacao(n1, n2):
    m = n1 * n2
    print(f'{n1} * {n2} = {m}')


def divisao(n1, n2):
    d = n1 / n2
    print(f'{n1} / {n2} = {d}')


while True:
    num1 = int(input('Valor do primeiro número: '))
    num2 = int(input('Valor do segundo número: '))

    menu()
    opcao = int(input('Selecione sua opção: '))

    match opcao:
        case 1:
            soma(num1, num2)
        case 2:
            subtracao(num1, num2)
        case 3:
            multiplicacao(num1, num2)
        case 4:
            divisao(num1, num2)
        case 5:
            print('Obrigado por utilizar o programa!')
            break
        case _:
            print('Opção inválida!')
    print('--' * 12)
