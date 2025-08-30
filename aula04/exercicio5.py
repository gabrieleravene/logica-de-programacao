# Escreva um algoritmo que calcule e exiba a tabuada de um número escolhido e digitado pelo usuário.
# A tabuada deve ser calculada até um determinado número n, também fornecido pelo usuário. Implemente o laço usando for

numero = int(input("Digite um número qualquer: "))
n = int(input("Digite um número qualquer: "))

for i in range(1, n+1):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado} ")