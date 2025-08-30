# app para empresa que vende planos de saúde

# informações do aluno

nome = "Gabriele Ravene"
print(f"Sistema desenvolvido por {nome}.")

# cálculo do valor mensal do plano: valorMensal = valorBase * porcentagem

# pergunta ao usuário valor base e idade do cliente
valorBase = int(input("Valor base do plano: "))
idade = int(input("Idade do cliente: "))

# define a porcentagem baseado na idade do cliente
if idade <= 19:
    porcentagem = 100/100
elif idade > 19 and idade <= 29:
    porcentagem = 150/100
elif idade > 29 and idade <= 39:
    porcentagem = 225/100
elif idade > 39 and idade <= 49:
    porcentagem = 240/100
elif idade > 49 and idade <= 59:
    porcentagem = 350/100
else:
    porcentagem = 600/100

# cálculo do valor mensal do plano
valorMensal = valorBase * (porcentagem)

# informa o resultado mensal do plano
if idade >= 29:
   print(f"Maior de 29 anos. O valor mensal do plano é: {valorMensal}")