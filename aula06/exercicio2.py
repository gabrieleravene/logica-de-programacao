# Escreva uma função que contenha dois parâmetros.
# Essa função recebe como parâmetro uma string com uma mensagem a ser impressa na tela, e outro parâmetro como sendo uma quantidade arbitrária de números empacotados.
# Dentro da função, encontre o maior dentre todos os números recebidos e escreva na tela, dentro da função, a mensagem e o maior valor.

def maior_num(str, *num):
    acumulador = 0
    print('Tupla: {}'.format(num))
    maior_numero = 0
    for i in num:
        if i > maior_numero:
            maior_numero = i
        acumulador += i
    print(f'o maior valor é: {maior_numero}!')
    return acumulador

print(maior_num("oi", 1, 2, 3))