# Faça um programa que pergunte ao usuário o seu salário e o seu tempo na empresa. Calcule a bonificação com base nos dados informados pelo usuário e imprima na tela o resultado.

salario = float(input("Salário: "))
tempo_empresa = int(input("Tempo na empresa: "))

if tempo_empresa > 5:
    bonus = salario * 0.2
else:
    bonus = salario * 0.1
    
print(f"Sua bonificação é de {bonus} e seu novo salário é {bonus + salario}.")