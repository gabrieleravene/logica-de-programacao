# informações do aluno
nome_completo = 'Gabriele Ravene'
print(f'Bem-vindos a Pizzaria de {nome_completo}')

# menu para o usuário
print('Opções: \n'
       'Tamanho P: Pizza Salgada (PS): 30 reais, Pizza Doce (PD): 35 reais; \n'
       'Tamanho M: Pizza Salgada (PS): 45 reais, Pizza Doce (PD): 48 reais; \n'
       'Tamanho G: Pizza Salgada (PS): 60 reais, Pizza Doce (PD): 66 reais;')

# acumulador 
soma = 0

while True:
  # entrada de dados para escolher sabor
    sabor = input('Digite o sabor desejado (PS ou PD): ')
    if sabor != 'PS' and sabor != 'PD':
        print('Valor inválido. Tente novamente.')
        sabor = input('Digite o sabor desejado: ')

# entrada de dados para escolher tamanho
    tamanho = input('Digite o tamanho desejado (P, M ou G): ')
    if tamanho != 'P' and tamanho != 'M' and tamanho != 'G':
       print('Tamanho inválido. Tente novamente.')
       tamanho = input('Digite o tamanho desejado: ')

# preço de acordo com sabor e tamanho informado
    if tamanho == 'P' and sabor == 'PS':
       valor = 30
    elif tamanho == 'P' and sabor == 'PD':
       valor = 34
    elif tamanho == 'M' and sabor == 'PS':
       valor = 45
    elif tamanho == 'M' and sabor == 'PD':
       valor = 48
    elif tamanho == 'G' and sabor == 'PS':
       valor = 60
    elif tamanho == 'G' and sabor == 'PD':
       valor = 66
  
    if sabor == 'PS':
        pizza_escolhida = 'Pizza Salgada'
    else:
       pizza_escolhida = 'Pizza Doce'

    print(f'Você pediu uma {pizza_escolhida}, tamanho {tamanho}, no valor de R${valor}.')
  
# soma o valor dos pedidos
    soma += valor

# verifica se o usuário deseja realizar mais pedidos
    mais_pedidos = input('Deseja fazer outro pedido? Responda com SIM ou NÃO.')
    if mais_pedidos == 'SIM':
        continue
    else:
        break
    
# saída de dados que imprime na tela o valor total a ser pago
print(f'O valor total dos pedidos é: R$ {soma} reais')