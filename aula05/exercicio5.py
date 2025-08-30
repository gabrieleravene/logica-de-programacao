#  Fatorial é um número inteiro positivo, representado por n!
# Calculamos a fatorial pela multiplicação desse número n por todos os seus antecessores até chegar em 1. Ainda, fatorial de 0! Sempre será 1.
# Considerando a breve explicação sobre fatorial, escreva uma função que calcule o fatorial de um número recebido como parâmetro e retorne o seu resultado.
# Faça uma validação dos dados por meio de uma outra função, permitindo que somente valores positivos sejam aceitos.

def validar_entrada(x):
    if x < 0:
        return False
    return True

def fat(x):
    if not validar_entrada(x):
        return "O número deve ser positivo ou zero."
    
    if x == 0:
        return 1
       
    resultado = 1
    for i in range(1, x + 1):
        resultado *= i
    return resultado