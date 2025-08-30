# Faça um algoritmo que receba três valores, representando os lados de um triângulo fornecidos pelo usuário.
# Verifique se os valores formam um triângulo e classifique como:
# a) Equilátero (três lados iguais);
# b) Isósceles (dois lados iguais);
# c) Escaleno (três lados diferentes).
# Lembre-se de que, para formar um triângulo, nenhum dos lados pode ser igual a zero e um lado não pode ser maior do que a soma dos outros dois.

a = int(input("Primeiro lado: "))
b = int(input("Segundo  lado: "))
c = int(input("Terceiro lado : "))

if a == 0 or b == 0 or c == 0 or a > (b+c) or b > (a+c) or c > (a+b):
    print("Digite um valor válido.")
else:
    if a == c and c == b:
       print("É um triâgulo equilátereo.")
    elif a == c or a == b or b == c:
       print("É um triângulo isósceles.")
    else:
        print("É um triângulo escaleno.")