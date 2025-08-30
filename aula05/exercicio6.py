# Exercício 3 (adaptado de Puga; Risseti, 2016, p. 117)
# Faça uma função que recebe dois valores inteiros e positivos como parâmetro.
# Calcule a soma dos n valores inteiro existentes entre eles, inclusive estes números.

def soma(a, b):
    soma = 0
    for i in range(a, b + 1):
        soma += i
    return soma

print(soma(10, 20))