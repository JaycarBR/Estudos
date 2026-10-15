"""Escreva um módulo que contenha uma função que receba os
comprimentos dos dois lados mais curtos de um triângulo
retângulo (catetos) como seus parâmetros. A função deve
retornar a hipotenusa do triângulo, calculada usando o
teorema de Pitágoras.
Escreva também o programa principal que recebe do usuário
os comprimentos dos catetos do triângulo retângulo, chama a
função para calcular a hipotenusa e exibe o resultado."""

def hipotenusa(a, b):
    from math import sqrt
    hip=sqrt(a**2+b**2)
    print(hip)
    return hip