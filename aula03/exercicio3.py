# Um aluno, para passar de ano, precisa estar aprovado em todas as matérias que ele está cursando.
# Assuma que a média para aprovação é a partir de 7, e que o aluno cursa 3 matérias, somente. Escreva um algoritmo que leia a nota final do aluno em cada matérias, e informe na tela se ele passou de ano, ou não. 

nota1 = int(input("Nota da primeira matéria: "))
nota2 = int(input("Nota da segunda matéria: "))
nota3 = int(input("Nota da terceira matéria: "))

if nota1 >=7 and nota2 >= 7 and nota3 >= 7:
    print("Você está aprovado! :)")
else:
    print("Você está reprovado! :(")