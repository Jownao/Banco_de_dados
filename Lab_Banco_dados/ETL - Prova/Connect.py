'''import psycopg2

conn = psycopg2.connect(
    host=localhost,
    database=teste_py,
    user=postgres,
    password=admin)'''

import cx_Oracle

try:
    conn = cx_Oracle.connect(
    user = 'admin',
    password = 'admin',
    dsn = 'localhost/xe')
except Exception as erro:
    print('Erro de conexão com o banco', erro)
else:
    print('Conectado ao Oracle Database', conn.version)

sql = conn.cursor()
texto = input('Digite a consulta: ')
sql.execute(texto)

result = sql.fetchall()
print(result)

conn.close()

