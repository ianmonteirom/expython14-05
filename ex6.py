"""
6. Implementar uma função que recebe como parâmetro a altura em metros (exemplo: 1.70) e o sexo
('M' para masculino e 'F' para feminino) de uma pessoa e retorne o seu peso ideal, sendo que:
Peso Ideal (para homens) = (72.7 * altura) - 58
Peso Ideal (para mulheres) = (62.1 * altura) - 44.7
"""


def peso_ideal(a, s):
    if s == 'm':
        ideal = (72.7 * a) - 58
    elif s == 'f':
        ideal = (62.1 * a) - 44.7
    return ideal


altura = float(input('Altura: '))
sexo = str(input('Sexo [M/F]: ')).strip().lower()

print(f'Peso ideal: {peso_ideal(altura, sexo):.2f} kg')
