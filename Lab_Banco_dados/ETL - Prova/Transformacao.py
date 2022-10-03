import pandas as pd
import cx_Oracle
from Delete import *

try:
    conn = cx_Oracle.connect(
    user = 'admin',
    password = 'admin',
    dsn = 'localhost/xe')
    sql = conn.cursor()
except Exception as erro:
    print('Erro de conexão com o banco', erro)


def cargaAlunos():
    df = pd.read_sql('''SELECT MAT_ALU, NOME, TO_CHAR(DAT_ENTRADA) AS DAT_ENTRADA, COD_CURSO,COTISTA  FROM alunos''',conn)
    # Loop de inserção
    deleteDimensaoAlunos()
    for i, mat_alu in enumerate(df['MAT_ALU']):
        nome = df.loc[i,'NOME']
        dat_entrada = df.loc[i,'DAT_ENTRADA']
        cod_curso = df.loc[i,'COD_CURSO']
        cotista = df.loc[i,'COTISTA']
            
        script = 'INSERT INTO DM_ALUNOS (MAT_ALU,NOME,DAT_ENTRADA,COD_CURSO,COTISTA) VALUES ('''

        dat_entrada = str(dat_entrada).replace('[','').replace(']','')

        dados = str(mat_alu) + ',' + '\'' + nome + '\',' + '\'' + dat_entrada + '\',' + str(cod_curso) + ',' + '\'' + cotista + '\'' + ')'
                
        query = script + dados
        #print(query)
        sql.execute(query)
        conn.commit()

def cargaCursos():
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
        conn.commit()


def cargaDepartamentos():
    df = pd.read_sql('''SELECT * from DEPARTAMENTOS''',conn)
    # Loop de inserção 
    deleteDimensaoDep()
    for i, COD_DPTO in enumerate(df['COD_DPTO']):
        nome_dpto = df.loc[i,'NOME_DPTO']
        cod_dpto = df.loc[i,'COD_DPTO']
        script = 'INSERT INTO DM_DEPARTAMENTOS (COD_DPTO,NOME_DPTO) VALUES ('''

        dados = str(cod_dpto) + ',' + '\'' + nome_dpto + '\''+ ')'
        query = script + dados
        #print(query)
        sql.execute(query)
        conn.commit()


def cargaDisciplinas():
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
        conn.commit()


def cargaMatriculas():
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
        conn.commit()

def cargaFato():
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
        conn.commit()

        

