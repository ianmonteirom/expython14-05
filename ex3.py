"""
3. Crie uma função que recebe como parâmetro um número inteiro e retorna o seu dobro.
"""


def dobro(num):
    d = num * 2
    return d


n = int(input('Número inteiro: '))

print(f'Dobro de {n}: {dobro(n)}')
