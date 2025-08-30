# Escreva um algoritmo que leia dois valores numéricos e que pergunte ao usuário qual operação ele deseja realizar: adição (+), subtração (-), multiplicação (*) ou divisão (/). Exiba na tela o resultado da operação desejada.

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

print(""" OPERAÇÃOES:
      SUBTRAÇÃO: - 
      ADIÇÃO: +
      MULTIPLICAÇÃO: *
      DIVISÃO: / """)
opcao = input("Qual operação deseja realizar?")

if opcao == "-":
    resultado = valor1 - valor2
elif opcao == "+":
    resultado = valor1 + valor2
elif opcao == "*":
    resultado = valor1 * valor2
elif opcao == "/":
    resultado = valor1 / valor2
else:
    print("Opção inválida.")
    
print(f"O resultado dos valores fornecidos é {resultado}.")