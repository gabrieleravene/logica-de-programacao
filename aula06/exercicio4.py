#  Escreva um algoritmo que leia o nome, a altura e o peso de pessoas, e armazene as informações em uma lista.
# O programa deve cadastrar um número indeterminado de dados e armazenar dentro da lista também o IMC da pessoa.
# Ao final do programa, imprima a lista completa e também:
# • o total de cadastros;
# • a pessoa com o maior IMC;
# • a pessoa com o menor IMC.
# O cálculo do IMC deve ser realizado empregando uma função lambda e é dado como: IMC = peso / (altura²).

dados = []
imc = lambda peso, altura: peso / (altura * altura)


while True:
    nome = input("Nome: ")
    altura = float(input("Altura: "))
    peso = float(input("Peso: "))
    x = imc(peso, altura)
    dados.append([nome, altura, peso, x])
    
    continuar = input('Deseja fazer mais cadastros? (s/n)')
    if continuar == 'n':
        break

print(f"Cadastro: {dados}")
print(f"Total de cadastros: ', {len(dados)}")

maior = 0
menor = 99
for item in dados:
    if item[3] > maior:
        maior = item[3]
    if item[3] > menor:
        menor = item[3]

print(f'Maior IMC: {maior}')
print(f'Menor IMC: {menor}')