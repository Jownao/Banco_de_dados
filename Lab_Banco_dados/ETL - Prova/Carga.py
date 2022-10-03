# Importando módulos
import cx_Oracle
import pandas as pd
import sys
from Delete import *
from Transformacao import *

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

def carga():
    # Conectar a uma database existente
    try:
        conn = cx_Oracle.connect(
        user = 'admin',
        password = 'admin',
        dsn = 'localhost/xe')
    except Exception as erro:
        print('Erro de conexão com o banco', erro)
    else:
        print('Conectado ao Oracle Database', conn.version)

    # Cursor da conexão
    sql = conn.cursor()

    # Executar um comando SQL
    try:

        comando = input('1 - Inserir e Consultar\n2 - ETL\n')

        if comando == '1':
            comando=input('')
            sql.execute(comando)
            result = sql.fetchall()
            for resultado in result:
                print(resultado)
        elif comando == '2':
            deleteDimensaoFato()
            # Carga DM_ALUNOS
            cargaAlunos()   
            print('Carga DM_ALUNOS concluída com sucesso!')
                
            # Carga DM_CURSOS
            cargaCursos() 
            print('Carga DM_CURSOS concluída com sucesso!')

            # Carga DM_DEPARTAMENTOS
            cargaDepartamentos()         
            print('Carga DM_DEPARTAMENTOS concluída com sucesso!')

            # Carga DM_DISCIPLINAS
            cargaDisciplinas()
            print('Carga DM_DISCIPLINAS concluída com sucesso!')

            # Carga DM_MATRICULAS
            cargaMatriculas()
            print('Carga DM_MATRICULAS concluída com sucesso!')

            #Carga FT_FATO
            cargaFato()
            print('Carga FT_FATO concluída com sucesso!')
            conn.commit()

        conn.close()
    except Exception as erro:
        print('Erro na execução do comando', erro)
        conn.close()


