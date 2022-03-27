from operator import truediv
import os
from ssl import OP_ENABLE_MIDDLEBOX_COMPAT 
import dbFunctions
import time

#funcao para listar opcoes ao usuario
def listarOpcoes():
    x = 0
    opcoes = ['Cadastrar novo funcionário.','Listar Funcionários.','Alterar cadastro de funcionário.','Deletar um funcionário.','Sair']
    print('Cadastro e controle de funcionários\n')
    print('Opções:')
    while x < 5:
            print(f'{x+1} - {opcoes[x]}')
            x+=1

#Validacao Valores digitados
def validaOpcao():
    try:
        Useropcao = int(input('Informe a opção desejada: '))
        if Useropcao < 1 or Useropcao > 5:
            print('Valor informado não é uma opção válida. Reiniciando em 3 segundos!')
            time.sleep(3)
            return 0 
        else:
            return Useropcao
    except:
        print('Valor informado não é uma opção válida. Reiniciando em 3 segundos!')
        time.sleep(3)
        return 0

#Chamando funcao de configuracao e conexão ao banco de dados 
dbFunctions.cnnStart()

#limpando tela
os.system('cls')

opcao=0
# Programa Principal
while True:
    listarOpcoes()
    opcao = validaOpcao()
    
    if opcao == 0:
        continue
    else:
        if opcao == 1:
            
            nome_func = input('Informe o nome do funcionario: ')
            data_nascimento = input('Informe a data de nascimento (DD/MM/AAAA): ')
            cpf_func = input('Informe o CPF do funcionario(sem pontos ou traços): ')
            email_func = input('Informe o e-mail do funcionario: ')

            funcionario = {
               'NOME' : nome_func,
               'DATA_NASCIMENTO' : data_nascimento,
               'CPF': cpf_func,
               'EMAIL': email_func
           }
           
            print('Validação de dados para efetuar cadastro:')

            for chave, valor  in funcionario.items():
                print(f'{chave} : {valor}')

            confirmacao = input('Confirma o cadastro? (S para sim /N para não): ')

            if confirmacao in ('s','S'):

                retornoFuncao = dbFunctions.cadastrarFunc(funcionario)
                
                if retornoFuncao == 1:
                   print('CPF JÁ EXISTENTE, REINICIANDO!')
                   time.sleep(3)
                   continue
                else:
                    print('Cadastrado com sucesso!\n')
                    
                    resposta = input('Deseja fazer mais alguma operação? S para sim / N para Nao: ')
                    if resposta in ('s','S'):
                        continue
                    else:
                        break
            else:
                print('Cadastro cancelado! Retornando a tela inicial em 3 segundos!')
                time.sleep(3)
                continue

        elif opcao == 2:
            print('\n')
            dados = dbFunctions.listarFunc()

            print('Listando Cadastro Funcionários')

            print('NOME | DATA NASCIMENTO | CPF | EMAIL')

            for funcionario in dados:
                nome, data_nascimento, cpf, email = funcionario
                print(f'{nome} | {data_nascimento} | {cpf} | {email} |')
            print('\n')
                
        elif opcao == 3:
            'Logica para alterar'
        elif opcao == 4:
            'Logica para deletar'
        elif opcao == 5:
            print('Finalizando o programa!\n')
            break            