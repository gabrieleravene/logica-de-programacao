# Escreva um algoritmo que repetidamente pergunte ao usuário qual sua idade e seu sexo (M ou F). Para cada resposta o programa deve responder imprimir a mensagem:
# “Boa noite, Senhor. Sua idade é <IDADE>” caso gênero masculino ou
# “Boa noite, Senhora. Sua idade é <IDADE>” caso gênero feminino.
# O programa deve encerrar quando o usuário digitar uma idade negativa.

idade = int(input("Qual sua idade?"))
sexo = input("Qual seu sexo? (M/F)").strip().lower()

while idade > 0:
    if sexo == 'f':
       print(f"Boa noite senhora, sua idade é {idade}.")
    elif sexo == 'm':
        print(f"Boa noite senhor, sua idade é {idade}.")
    else:
        print("Valor inválido.")
        
    idade = int(input("Qual sua idade?"))
    sexo = input("Qual seu sexo? (M/F)").strip().lower()