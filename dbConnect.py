import psycopg2
from convertRtf import convertRtfToText


def updateRow(texto, prontuario_id, cursor):
    query = """update t_pacientesevolucoes 
    set texto = %s,
    convertido = true
    where id = %s;"""

    cursor.execute(query, (texto, prontuario_id))

connection = psycopg2.connect("dbname=newcristiano user=postgres password=postgres port=5433")
cursor = connection.cursor()

cursor.execute("select id, texto, convertido from t_pacientesevolucoes where convertido is not true")
obj = cursor.fetchall()

for row in obj:
    prontuario_id = row[0]
    rtf = row[1]
    text = convertRtfToText(rtf)
    updateRow(text, prontuario_id, cursor)

connection.commit()
cursor.close()
connection.close()
