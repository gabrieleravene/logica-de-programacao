import copy

# informações do aluno
nome_completo = 'Gabriele Ravene'
print(f'Bem vindos à lista de contatos de {nome_completo}')

# lista de contatos e id_global
lista_contatos = []
id_global = 5003063

# função para cadastrar contato
def cadastrar_contato(id):
    nome = input('Insira o nome do contato: ')
    atividade = input('Insira a atividade do contato: ')
    telefone = input('Insira o telefone do contato: ')

    contato = {
        "id": id,
        "nome": nome,
        "atividade": atividade,
        "telefone": telefone
    }

    lista_contatos.append(copy.deepcopy(contato))
    print(f'Contato {nome} cadastrado.')
# função para consultar contatos
def consultar_contatos():
    while True:
        print('1\nEscolha uma opção:')
        print('1. Consultar Todos')
        print('2. Consultar por Id')
        print('3. Consultar por Atividade')
        print('4. Retornar ao menu')

        opcao = input('Opção: ')

        if opcao == '1':
            for contato in lista_contatos:
                print(contato)
        elif opcao == '2':
            id_consulta = int(input('Informe o ID do contato: '))
            contato = next((c for c in lista_contatos if c["id"] == id_consulta), None)
            if contato:
                print(contato)
            else:
                print('Contato não encontrado.')
        elif opcao == '3':
            atividade_consulta = input('Informe a atividade: ')
            contatos_filtrados = [c for c in lista_contatos if c["atividade"] == atividade_consulta]
            if contatos_filtrados:
                for contato in contatos_filtrados:
                    print(contato)
            else:
                print('Nenhum contato encontrado para essa atividade.')
        elif opcao == '4':
            return
        else:
            print('Opção inválida.')

# função para remover contato
def remover_contato():
    while True:
        id_remover = int(input('Informe o ID do contato a ser removido: '))
        contato = next((c for c in lista_contatos if c["id"] == id_remover), None)
        if contato:
            lista_contatos.remove(contato)
            print(f"Contato {contato['nome']} removido.")
            return
        else:
            print("ID inválido. Tente novamente.")

# estrutura principal
while True:
    print('\nMenu Principal:')
    print('1. Cadastrar Contato')
    print('2. Consultar Contato')
    print('3. Remover Contato')
    print('4. Encerrar Programa')

    opcao_menu = input('Opção: ')

    if opcao_menu == '1':
        id_global += 1
        cadastrar_contato(id_global)
    elif opcao_menu == '2':
        consultar_contatos()
    elif opcao_menu == '3':
        remover_contato()
    elif opcao_menu == '4':
        print("Encerrando programa...")
        break
    else:
        print('Opção inválida.')

# Saídas de console para cumprimento das exigências
# Exigência de Saída de Console 1: Cadastro do seu contato
cadastrar_contato(123456789)  # Nome: Seu Nome Completo, Atividade: Estudante, Telefone: Seu RU

# Exigência de Saída de Console 2: Cadastro de mais dois contatos
cadastrar_contato(123456790)  # Nome: Contato 1, Atividade: Marceneiro, Telefone: 111111111
cadastrar_contato(123456791)  # Nome: Contato 2, Atividade: Marceneiro, Telefone: 222222222

# Exigência de Saída de Console 3: Consulta de todos os contatos
consultar_contatos()

# Exigência de Saída de Console 4: Consulta por código de um dos contatos
consultar_contatos()

# Exigência de Saída de Console 5: Consulta por atividade (marceneiro)
consultar_contatos()

# Exigência de Saída de Console 6: Remoção de um contato e consulta de todos os contatos
remover_contato()
consultar_contatos()