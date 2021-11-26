import psycopg2
from striprtf.striprtf import rtf_to_text

def updateRow(textConverted, primaryKey, cursor):
    query = "update " + table_name + " set " + column_name + "= %s , where " + primary_key_column_name + " = %s ;"
    cursor.execute(query, (textConverted, primaryKey))

table_name = input("enter the name of the table containing the column to be converted: ")
column_name = input("Insert the column name to be converted: ")
primary_key_column_name = input("Insert the primary key column of the table (ex.: id): ")
db_name = input("Insert the postgres db name: ")
user = input("Insert the user: ")
password = input("Insert the password of db: ")
port = input("Insert the postgres port: ")

connection_str = "dbname="+db_name+" user="+user+" password="+password+" port="+port
con = psycopg2.connect(connection_str)
cur = con.cursor()

query = "select " + primary_key_column_name + ", " + column_name + " from " + table_name

cur.execute(query)
rows = cur.fetchall()

for row in rows:
    id = row[0]
    rtf = row[1]
    text = rtf_to_text(rtf)
    updateRow(text, id, cur)

con.commit()
cur.close()
con.close()
