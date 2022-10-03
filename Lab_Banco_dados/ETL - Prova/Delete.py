import cx_Oracle

# Deletar dimensão alunos
def deleteDimensaoALunos():
    try:
        conn = cx_Oracle.connect(
        user = 'admin',
        password = 'admin',
        dsn = 'localhost/xe')

        sql = conn.cursor()

        query = 'DELETE FROM DM_ALUNOS'
        sql.execute(query)
        conn.commit()
        conn.close()
    except Exception as erro:
        print('Erro de conexão com o banco', erro)

def deleteDimensaoCurso():
    try:
        conn = cx_Oracle.connect(
        user = 'admin',
        password = 'admin',
        dsn = 'localhost/xe')

        sql = conn.cursor()

        query = 'DELETE FROM DM_CURSOS'
        sql.execute(query)
        conn.commit()
        conn.close()
    except Exception as erro:
        print('Erro de conexão com o banco', erro)

def deleteDimensaoDep():
    try:
        conn = cx_Oracle.connect(
        user = 'admin',
        password = 'admin',
        dsn = 'localhost/xe')

        sql = conn.cursor()

        query = 'DELETE FROM DM_DEPARTAMENTOS'
        sql.execute(query)
        conn.commit()
        conn.close()
    except Exception as erro:
        print('Erro de conexão com o banco', erro)

def deleteDimensaoDisc():
    try:
        conn = cx_Oracle.connect(
        user = 'admin',
        password = 'admin',
        dsn = 'localhost/xe')

        sql = conn.cursor()

        query = 'DELETE FROM DM_DISCIPLINAS'
        sql.execute(query)
        conn.commit()
        conn.close()
    except Exception as erro:
        print('Erro de conexão com o banco', erro)

def deleteDimensaoMat():
    try:
        conn = cx_Oracle.connect(
        user = 'admin',
        password = 'admin',
        dsn = 'localhost/xe')

        sql = conn.cursor()

        query = 'DELETE FROM DM_MATRICULAS'
        sql.execute(query)
        conn.commit()
        conn.close()
    except Exception as erro:
        print('Erro de conexão com o banco', erro)

def deleteDimensaoFato():
    try:
        conn = cx_Oracle.connect(
        user = 'admin',
        password = 'admin',
        dsn = 'localhost/xe')

        sql = conn.cursor()

        query = 'DELETE FROM FT_FATO'
        sql.execute(query)
        conn.commit()
        conn.close()
    except Exception as erro:
        print('Erro de conexão com o banco', erro)