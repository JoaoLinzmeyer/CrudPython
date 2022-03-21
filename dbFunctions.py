import sqlite3

def cnnStart(): 
    #String de conexão ao sqlite, caso esse banco não exista ele cria!
    global cnn
    cnn = sqlite3.connect("./DB/funcionarios.db")

    #criando o cursor
    global cursor 
    cursor = cnn.cursor()

    #Criando a tabela dentro do banco caso ela não exista
    query = """ 
        create table if not exists cad_funcs 
        (nome_func varchar(30)not null, nasc_data date not null, cpf_func varchar(11) not null, email_func varchar(30) not null)
    """
    cursor.execute(query)

    #Verificando se existe algum usuario admin, caso não, realizado a criação

    query = """
        select count(*) from cad_funcs where nome_func='admin'
    """
    cursor.execute(query)
    data = cursor.fetchall()
    qtdRegistro = data[0][0] 

    if not qtdRegistro:
        query = "insert into cad_funcs (nome_func,nasc_data,cpf_func,email_func) values ('admin','1900-01-01','00000000000','admin@admin.com.br')";
        cursor.execute(query)
        cnn.commit()

def cpfExiste(cpf):
    query = f"select count(*) from cad_funcs where cpf_func='{cpf}'" 
    cursor.execute(query)
    data = cursor.fetchall()
    if data[0][0] > 0:
        return True
    else:
        return False


def cadastrarFunc(funcionario):
    print(funcionario)

    validacao = cpfExiste(funcionario['CPF'])

    if validacao:
       return 1 #erro 1 = CPF JA CADASTRADO
    else:
       query = f"insert into cad_funcs (nome_func,nasc_data,cpf_func,email_func) values ('{funcionario['NOME']}','{funcionario['DATA_NASCIMENTO']}',{funcionario['CPF']},'{funcionario['EMAIL']}')"
       cursor.execute(query)
       cnn.commit()
       data = cursor.fetchall()
       print(data)