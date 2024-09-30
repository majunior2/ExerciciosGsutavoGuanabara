"""
Faça um programa que leia  o comprimento do cateto oposto e cateto adjacente de um triângulo retângulo,
calcule e mostre o comprimento da hipotenusa.
"""
from math import hypot
co = float(input('Comprimento do  cateto oposto: ')) 
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hpitenusa  vai medir{:.2f}'.format(hi))
