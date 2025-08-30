# Escreva uma rotina que recebe três valores como parâmetro e coloque-os em ordem crescente, ou seja, o menor ao maior. Imprima na tela os três valores.

def crescente(a=0, b=0, c=0):
    if a and b and c:
        if  a > b and a > c:
            if b > c:
                print(f'ordem crescente: {c}, {b}, {a}')
            else:
                print(f'ordem crescente: {b}, {c}, {a}')
        elif b > a and b > c:
            if a > c:
                print(f'ordem crescente: {c}, {a}, {b}')
            else:
                print(f'ordem crescente: {a}, {c},  {b}')
        elif c > a and c > b:
            if a > b:
                print(f'ordem crescente: {b}, {a}, {c}')
            else:
                print(f'ordem crescente: {a}, {b}, {c}')