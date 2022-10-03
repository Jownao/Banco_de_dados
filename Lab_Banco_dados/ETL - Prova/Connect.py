# importando o módulo
import cx_Oracle
import pandas as pd
from Delete import *
import sys

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

        comando = input('1 - Inserir\n2 - Consultar\n3 - ETL\n')

        if comando == '1':
            comando=input('')
            sql.execute(comando)

        elif comando == '2':
            comando=input('')
            sql.execute(comando)
            result = sql.fetchall()
            for i in result:
                print(i)
            #print(result)
        elif comando == '3':
            deleteDimensaoFato()
            # Carga DM_ALUNOS

            df = pd.read_sql('''SELECT MAT_ALU, NOME, TO_CHAR(DAT_ENTRADA) AS DAT_ENTRADA, COD_CURSO,COTISTA  FROM alunos''',conn)
            # Loop de inserção
            deleteDimensaoALunos()
            for i, mat_alu in enumerate(df['MAT_ALU']):
                nome = df.loc[i,'NOME']
                dat_entrada = df.loc[i,'DAT_ENTRADA']
                cod_curso = df.loc[i,'COD_CURSO']
                cotista = df.loc[i,'COTISTA']
                
                script = 'INSERT INTO DM_ALUNOS (MAT_ALU,NOME,DAT_ENTRADA,COD_CURSO,COTISTA) VALUES ('''

                dat_entrada = str(dat_entrada).replace('[','').replace(']','')

                dados = str(mat_alu) + ',' + '\'' + nome + '\',' + '\'' + dat_entrada + '\',' + str(cod_curso) + ',' + '\'' + cotista + '\'' + ')'
                
                query = script + dados
                sql.execute(query)
                
            print('Carga DM_ALUNOS concluída com sucesso!')
                
            # Carga DM_CURSOS

            df = pd.read_sql('''SELECT * from cursos''',conn)
            # Loop de inserção
            deleteDimensaoCurso()
            for i, COD_CURSO in enumerate(df['COD_CURSO']):
                cod_curso = df.loc[i,'COD_CURSO']
                nom_curso = df.loc[i,'NOM_CURSO']
                cod_dpto = df.loc[i,'COD_DPTO']

                script = 'INSERT INTO DM_CURSOS (COD_CURSO,NOM_CURSO,COD_DPTO) VALUES ('''

                dados = str(cod_curso) + ',' + '\'' + nom_curso + '\',' + str(cod_dpto) + ')'
                
                query = script + dados
                #print(query)
                sql.execute(query)
                
            print('Carga DM_CURSOS concluída com sucesso!')

            # Carga DM_DEPARTAMENTOS

            df = pd.read_sql('''SELECT * from DEPARTAMENTOS''',conn)
            # Loop de inserção
            deleteDimensaoDep()
            for i, COD_DPTO in enumerate(df['COD_DPTO']):
                NOME_DPTO = df.loc[i,'NOME_DPTO']
                cod_dpto = df.loc[i,'COD_DPTO']

                script = 'INSERT INTO DM_DEPARTAMENTOS (COD_DPTO,NOME_DPTO) VALUES ('''

                dados = str(cod_dpto) + ',' + '\'' + NOME_DPTO + '\''+ ')'
                query = script + dados
                #print(query)
                sql.execute(query)
                
            
            print('Carga DM_DEPARTAMENTOS concluída com sucesso!')

            # Carga DM_DISCIPLINAS

            df = pd.read_sql('''SELECT * from DISCIPLINAS''',conn)
            # Loop de inserção
            deleteDimensaoDisc()
            for i, COD_DPTO in enumerate(df['COD_DISC']):
                cod_disc = df.loc[i,'COD_DISC']
                nome_disc = df.loc[i,'NOME_DISC']
                carga_horaria = df.loc[i,'CARGA_HORARIA']

                script = 'INSERT INTO DM_DISCIPLINAS (COD_DISC,NOME_DISC,CARGA_HORARIA) VALUES ('''

                dados = str(cod_disc) + ',' + '\'' + nome_disc + '\',' + str(carga_horaria) + ')'
                query = script + dados
                #print(query)
                sql.execute(query)
            print('Carga DM_DISCIPLINAS concluída com sucesso!')

            # Carga DM_MATRICULAS

            df = pd.read_sql('''SELECT DISTINCT SEMESTRE from MATRICULAS''',conn)
            # Loop de inserção
            deleteDimensaoMat()
            for i, SEMESTRE in enumerate(df['SEMESTRE']):
                semestre = df.loc[i,'SEMESTRE']

                script = 'INSERT INTO DM_MATRICULAS (SEMESTRE) VALUES ('''
                
                dados = str(semestre) + ')'
                query = script + dados
                #print(query)
                sql.execute(query)
            print('Carga DM_MATRICULAS concluída com sucesso!')

            #Carga FT_FATO

            df = pd.read_sql('''SELECT A.MAT_ALU,SEMESTRE,C.COD_CURSO,COD_DPTO,COD_DISC,NOTA,FALTAS,STATUS FROM ALUNOS A JOIN CURSOS C ON A.COD_CURSO = C.COD_CURSO JOIN MATRICULAS M ON A.MAT_ALU = M.MAT_ALU''',conn)
            # Loop de inserção
            
            for i, MAT_ALU in enumerate(df['MAT_ALU']):
                mat_alu = df.loc[i,'MAT_ALU']
                semestre = df.loc[i,'SEMESTRE']
                cod_curso = df.loc[i,'COD_CURSO']
                cod_dpto = df.loc[i,'COD_DPTO']
                cod_disc = df.loc[i,'COD_DISC']
                nota = df.loc[i,'NOTA']
                faltas = df.loc[i,'FALTAS']
                status = df.loc[i,'STATUS']

                script = 'INSERT INTO FT_FATO (MAT_ALU,SEMESTRE,COD_CURSOs,COD_DPTO,COD_DISC,NOTA,FALTAS,STATUS) VALUES ('''

                dados = str(mat_alu) + ',' + str(semestre) + ',' + str(cod_curso) + ',' + str(cod_dpto) + ',' + str(cod_disc) + ',' + str(nota) + ',' + str(faltas) + ',' + '\'' + status + '\'' + ')'
                query = script + dados
                #print(query)
                sql.execute(query)
            print('Carga FT_FATO concluída com sucesso!')

        conn.commit()
        conn.close()
    except Exception as erro:
        print('Erro na execução do comando', erro)
        conn.close()


