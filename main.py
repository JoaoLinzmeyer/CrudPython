import os
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

#listar formatacao
def listarFuncionarioFormat(dados):
    print('\nNOME | DATA NASCIMENTO | CPF | EMAIL')

    for funcionario in dados:
        nome, data_nascimento, cpf, email = funcionario
        print(f'{nome} | {data_nascimento} | {cpf} | {email} ')
    print('\n') 

def confirma(frase):
    
    while True:
        res = input(f'{frase} (S - sim | N - NAO): ')
        if res not in ('s','S','n','N'):
            continue
        else:
            break
    return res


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

            confirmacao = confirma('Confirma o cadastro?')

            if confirmacao in ('s','S'):

                valCpf = dbFunctions.cpfExiste(funcionario['CPF'])
                               
                if valCpf:
                   print('CPF JÁ EXISTENTE, REINICIANDO!')
                   time.sleep(3)
                   continue
                else:
                    retornoFuncao = dbFunctions.cadastrarFunc(funcionario)
                    print('Cadastrado com sucesso!\n')
                    
                    # resposta = input('Deseja fazer mais alguma operação? S para sim / N para Nao: ')
                    # if resposta in ('s','S'):
                    #     continue
                    # else:
                    #     break
            else:
                print('Cadastro cancelado! Retornando a tela inicial em 3 segundos!')
                time.sleep(3)
                continue

        elif opcao == 2:
            print('\n')
            dados = dbFunctions.listarFunc()

            print('Listando Cadastro Funcionários')
            listarFuncionarioFormat(dados)
    
        elif opcao == 3:

            cpf_func = input('Informe o CPF do funcionário que deseja alterar os dados: ')

            valCpf = dbFunctions.cpfExiste(cpf_func)
            if valCpf:
                
                nome_func = input('Informe o nome do funcionario: ')
                data_nascimento = input('Informe a data de nascimento (DD/MM/AAAA): ')
                email_func = input('Informe o e-mail do funcionario: ')

                funcionario = {
                'NOME' : nome_func,
                'DATA_NASCIMENTO' : data_nascimento,
                'CPF': cpf_func,
                'EMAIL': email_func
                }

                dbFunctions.alterarFunc(funcionario)
                print('Dados alterados com sucesso!')

            else:
                print('Não existe funcionário cadastrado com o cpf informado!\n')

        elif opcao == 4:
            
            cpf_func = input('Informe o CPF do funcionário que deseja deletar: ')
            valCpf = dbFunctions.cpfExiste(cpf_func)
            
            if valCpf:
                dados = dbFunctions.listarFunc(cpf_func)
                listarFuncionarioFormat(dados)

                confirmacao = confirma('Confirma a exclusão?')
                if confirmacao in ('s','S'):
                    dbFunctions.delete(cpf_func)  
                else:
                    print('Ação cancelada!')
            else:
                print('Não existe funcionário cadastrado com o cpf informado!\n')
        elif opcao == 5:
            print('Finalizando o programa!\n')
