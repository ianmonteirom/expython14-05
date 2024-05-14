"""
4. Faça uma função que recebe um número inteiro por parâmetro e retorna True se for par e False se for ímpar.
"""


def par(num):
    if num % 2 == 0:
        return True
    else:
        return False


n = int(input('Digite um número: '))

print(f'Par? {par(n)}')
