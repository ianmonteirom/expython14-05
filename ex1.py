"""
1. Escreva um programa para solicitar as notas de duas provas. Faça uma função que receba as duas
notas por parâmetro e exibe a mensagem “Você foi Aprovado!” ou “Você foi Reprovado!”. Considere
6.0 a média mínima para aprovação.
"""


def calculo_media(n1, n2):
    if (n1 + n2) / 2 >= 6:
        return 'Você foi Aprovado!'
    else:
        return 'Você foi Reprovado!'


nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

print(calculo_media(nota1, nota2))
