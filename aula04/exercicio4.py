# Faça um programa que peça para o usuário digitar um valor inicial e final.
# Imprima na tela os números que neste intervalo de valor informado pelo usuário são:
# positivos e inteiros
# pares
# impares
# a soma dos números pares
# a soma dos números impares

valor_inicial = int(input("Digite um valor inicial: "))
valor_final = int(input("Digite valor final: "))
positivos_e_inteiros = []
pares = []
impares = []
soma_pares = 0
soma_impares = 0

for i in range(valor_inicial, valor_final+1):
    if i > 0:
        positivos_e_inteiros.append(i)
    if i % 2 == 0:
        pares.append(i)
    if i % 2 != 0:
        impares.append(i)
    
for i in pares:
    soma_pares += i

for i in impares:
    soma_impares += i
    
print(f"Os números positivos são: {positivos_e_inteiros}.")
print(f"Os números pares são: {pares}.")
print(f"Os números ímpares são: {impares}.")
print(f"A soma dos números pares são {soma_pares}.")
print(f"A soma dos números ímpares são: {soma_impares}.")        