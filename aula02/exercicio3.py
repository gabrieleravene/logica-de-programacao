# Desenvolva um algoritmo que solicite ao usuário o preço de um produto e um percentual de desconto a ser aplicado a ele. Calcule-o e exiba o valor do desconto e o preço final do produto.

preco = float(input("Preço do produto: "))
percentual_desconto = int(input("Percentual de desconto: "))

desconto = (preco * percentual_desconto) / 100

preco_final = preco - desconto
preco_final_arr = round(preco_final, 2)

print(f" valor do desconto é {desconto} e o preço final do produto é  {preco_final_arr}.")