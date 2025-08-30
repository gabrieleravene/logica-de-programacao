# Crie um programa que contenha uma tupla com o nome de 10 linguagens de programação: Javascript, Rust, Swift, Python, Kotlin, Go, C#, Dart, Julia e Typescript.
# Em qual posição está a linguagem Python? Mostre na tela.

def linguagens():
    ling = ('JavaScript', 'Rust', 'Swift', 'Python', 'Kotlin', 'Go', 'C#', 'Dart', 'Julia', 'TypeScript')
    
    i = 0
    
    while ling[i] !=  'Python':
        i += 1
    return f'A linguagem Python está na {i+1}ª posição.'