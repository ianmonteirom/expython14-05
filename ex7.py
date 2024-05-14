"""
7. Escreva um programa que solicita um valor inteiro ao usuário e exibe a tabuada doesse número. Você
deverá escrever as seguintes funções:
- ler_numero(): Solicita um número inteiro e retorna esse número para o programa principal.
- tabuada(n): Recebe como parâmetro um número inteiro e exibe na tela a tabuada desse número.
"""


def ler_numero():
    num = int(input('Digite um número para ver sua tabuada: '))
    return num


def tabuada(n):
    for i in range(1, 11):
        print(f'{n} x {i} = {n * i}')


tabuada(ler_numero())
