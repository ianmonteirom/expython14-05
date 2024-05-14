"""
5. Escreva um programa que leia o raio de um círculo e faça duas funções: uma função chamada area
que calcula e retorna a área do círculo e outra função chamada perimetro que calcula e retorna o
perímetro do círculo. Utilize as fórmulas abaixo
Área = π * r²
Perímetro = π * 2 * r
"""

from math import pi


def area(r):
    a = pi * r ** 2
    return a


def perimetro(r):
    p = pi * 2 * r
    return p


raio = float(input('Raio do círculo: '))

print(f'Área do círculo: {area(raio):.2f}\n'
      f'Perímetro do círculo: {perimetro(raio):.2f}')
