# O algoritmo mais simples de se buscar um dado em uma estrutura de dados é chamado de busca sequencial.
# A busca sequencial é uma varredura simples do primeiro ao último elemento da estrutura, verificando se o dado desejado se encontra presente.
# Escreva uma função em Python que receba como parâmetro uma lista e um dado.
# Verifique se o dado está presente na lista e retorne da função o seu índice, caso ele esteja presente. Caso contrário, retorne –1.

def verificar_dado(lista, dado):
    for indice, elemento in enumerate(lista):
        if elemento == dado:
            return indice
    return -1
        
minha_lista = [1, 2, 3]
