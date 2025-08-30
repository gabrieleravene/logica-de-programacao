# Faça um programa que solicita ao usuário seu ano de nascimento e o ano atual. Calcule a idade do usuário e verifique se ele já é maior de idade para tirar uma carteira de motorista. Imprima na tela a idade do usuário e o resultado.

ano_nascimento = int(input("Ano de nascimento: "))
ano_atual = int(input("Ano atual: "))

idade = ano_atual - ano_nascimento

if idade >= 18:
    print("Você tem {idade} anos. É maior de idade e já pode tirar carteira de motorista!")
else:
    print(f"Você tem {idade} anos, é menor de idade e ainda não pode tirar carteira de motorista.")