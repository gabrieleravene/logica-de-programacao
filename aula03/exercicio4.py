# Escreva um algoritmo em Python em que o usuário escolhe se ele quer comprar maçãs, laranjas ou bananas. Deverá ser apresentado na tela um menu com a opção 1 para maçã, 2 para laranja e 3 para banana.
# Após escolhida a fruta, deve-se digitar quantas unidades se quer comprar.
# O algoritmo deve calcular o preço total a pagar do produto escolhido e mostrá-lo na tela.
# Considere que uma maçã custa R$ 2,30, uma laranja R$ 3,60 e uma banana 1,85.

print(""" MENU:
      1 - Maçã 
      2 - Laranja
      3 - Banana """)

opcao = int(input("Digite qual fruta você deseja: "))
unidade = int(input("Qual quantidade deseja comprar?"))

if opcao == 1:
    print(f"Você deverá pagar R${unidade * 2.30}.")
elif opcao == 2:
    print(f"Você deverá pagar R${unidade * 3.60}.")
elif opcao == 3:
    print(f"Você deverá pagar R4{unidade * 1.85}.")