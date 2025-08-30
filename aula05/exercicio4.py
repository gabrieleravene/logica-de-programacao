# Escreva uma função para validar uma string. Essa função recebe como parâmetro a string, o número mínimo e máximo de caracteres.
# Retorne verdadeiro se o tamanho da string estiver entre os valores de mínimo e máximo, falso, caso contrário

def validar_str(str, min, max):
    if len(str) >= min and len(str) <= max:
        return True
    else:
        return False
        