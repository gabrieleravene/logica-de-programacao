# informações do aluno
nome_completo = 'Gabriele Ravene'
print(f'Bem-vindos a Madeireira da Lenhadora {nome_completo}')

# função para escolher o tipo de madeira
def escolha_tipo():
  opcoes = ['PIN', 'PER', 'MOG', 'IPE', 'IMB']

  print('Nossas opções são: \n'
          'Tora de Pinho (PIN) \n'
          'Tora de Peroboa (PER) \n'
          'Tora de Mogno (MOG) \n'
          'Tora de Ipê (IPE) \n'
          'Tora de Imbuia (IMB)')
  
  while True:
    tipo_de_madeira = input('Digite o tipo de madeira desejado (PIN/PER/MOG/IPE/IMB): ')
    if tipo_de_madeira in opcoes:
      return tipo_de_madeira 
    else:
      print('Opcão inválida. Tente novamente')

# função para usuário inserir quantidade de toras
def qtd_toras():
    valor_maximo = 2000
# validação de dados
    while True:
        try:
            quantidade_de_toras = int(input('Digite a quantidade de toras (m³): '))            
            if quantidade_de_toras < valor_maximo:
                if quantidade_de_toras < 100: 
                    desconto = 0
                elif 100 <= quantidade_de_toras < 500:
                    desconto = 0.4
                elif 500 <= quantidade_de_toras < 1000:
                    desconto = 0.9
                elif 1000 <= quantidade_de_toras < 2000:
                    desconto = 0.16
                
                return quantidade_de_toras, desconto 
            else:
                print('Digite um valor menor do que 2000.')
        
        except ValueError:
            print('Valor inválido. Por favor, digite um valor numérico.')

# função para usuário inserir tipo de transporte
def transporte():
  opcoes = [1, 2, 3]
  print('Qual o transporte desejado? \n'
          'Transporte rodoviário (1): R$ 1000 \n'
          'Transporte Ferroviário (2): R$ 2000 \n'
           'Transporte Hidroviário (3): R$ 2500')
# validação de dados
  while True:
      tipo_de_transporte = int(input('Digite o tipo de transporte (1, 2 ou 3): '))
      if tipo_de_transporte in opcoes:
        return tipo_de_transporte

      if tipo_de_transporte == 1:
        custo_do_transporte = 1000
      elif tipo_de_transporte == 2:
        custo_do_transporte = 2000
      elif tipo_de_transporte == 3:
        custo_do_transporte = 2500

      else:
        print('Valor inválido. Tente novamente.')

# função para calcular o total a ser pago
def total_pago(tipo_de_madeira, quantidade_de_toras, desconto, custo_do_transporte):
  if tipo_de_madeira == 'PIN':
    valor = 150.49
  elif tipo_de_madeira == 'PER':
    valor = 179.20
  elif tipo_de_madeira == 'MOG':
    valor = 190.90
  elif tipo_de_madeira == 'IPE':
    valor = 210.10
  else:
    valor = 220.70
    
  total_do_pedido = quantidade_de_toras * valor 
  pedido_com_desconto = total_do_pedido * (1 - desconto)
  total_a_ser_pago = pedido_com_desconto + custo_do_transporte

  return total_a_ser_pago

tipo_de_madeira = escolha_tipo()
quantidade_de_toras, desconto = qtd_toras()
custo_do_transporte = transporte()
total = total_pago(tipo_de_madeira, quantidade_de_toras, desconto, custo_do_transporte)
total_arredondado = round(total, 2)

print(f'O total a ser pago é R$ 1{total_arredondado}.')