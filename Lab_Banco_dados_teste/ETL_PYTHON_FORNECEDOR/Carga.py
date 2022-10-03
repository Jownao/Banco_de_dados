import mysql.connector 
from Transformacao import filiais_values_t, fornecedores_values_t, mercadorias_values_t

def carga():
    #Configurando conexão MySQL
    mydb = mysql.connector.connect( 
        host = "localhost", 
        user = "root", 
        password = "123456", 
        database = "fornecedor"
    )  

    #Criando o cursor para conexão    
    cursor = mydb.cursor()   
    reg_filial = reg_fornecedor = reg_mercadoria = 0
    #testanto se a conexão está OK
    if mydb.is_connected():

        try:
        
            #Carga Filiais
            sql = "INSERT into dm_filial (sk_filial, nk_filial, nome_filial) values (%s, %s, %s)"
            cursor.executemany(sql, filiais_values_t)
            reg_filial = cursor.rowcount
            
            #Carga Fornecedores
            sql = "INSERT into dm_fornecedor (sk_fornecedor,nk_fornecedor,cidade_fornecedor,uf_fornecedor,nome_fornecedor) values (%s, %s, %s, %s, %s)"
            cursor.executemany(sql, fornecedores_values_t)
            reg_fornecedor = cursor.rowcount
            
            #Carga Mercadorias
            sql = "INSERT into dm_mercadoria (sk_mercadoria,nk_mercadoria,nome_mercadoria) values (%s, %s, %s)"
            cursor.executemany(sql, mercadorias_values_t)   
            reg_mercadoria = cursor.rowcount       
                         
        except:
            mydb.rollback()

    mydb.commit() 
    print("Dados da Filiais Inseridos. ", reg_filial," registros.")   
    print("Dados dos Fornecedores Inseridos. ", reg_fornecedor," registros.")   
    print("Dados das Mercadorias Inseridos. ", reg_mercadoria," registros.") 
    mydb.close()

