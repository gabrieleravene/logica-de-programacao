# Escreva um algoritmo que leia dois valores e imprima na tela o resultado da multiplicação de ambos.
# Porém, para calcular a multiplicação, utilize somente operações de soma e subtração.

multiplicando = int(input("Digite o primeio valor: "))
multiplicador = int(input("Digite o segundo valor: "))

resultado = 0

for i in range (multiplicador):
    resultado += multiplicando
print(resultado)