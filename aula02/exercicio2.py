# Faça um programa que solicite ao usuário quantidade de dias, horas, minutos e segundos. calcule o total de segundos resultante e imprima-o na tela, para o usuário.

dias = int(input("Digite uma quantidade de dias: "))
horas = int(input("DIgite uma quantidade de horas: "))
minutos = int(input("Digite uma quantidade de minutos: "))
segundos =int(input("Digite uma quantidade de segundos: "))

total_segundos = segundos + (minutos * 60) + (horas * 3600) + (dias * 86400)

print(f"O total de segundos dos valores fornecidos é {total_segundos}.")