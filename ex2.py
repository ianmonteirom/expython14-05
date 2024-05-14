"""
2. Faça uma função que receba como parâmetro o número de lados de um polígono e:
- Se o número de lados for igual a 3, escrever TRIÂNGULO.
- Se o número de lados for igual a 4, escrever QUADRILÁTERO.
- Se o número de lados for igual a 5, escrever PENTÁGONO.
- Se o número de lados for diferente de 3, 4 ou 5, escrever VALOR INVÁLIDO
"""


def num_lados(nl):
    match nl:
        case 3:
            return 'TRIÂNGULO'
        case 4:
            return 'QUADRILÁTERO'
        case 5:
            return 'PENTÁGONO'
        case _:
            return 'VALOR INVÁLIDO'


n = int(input('Digite o número de lados do polígono: '))

print(num_lados(n))
