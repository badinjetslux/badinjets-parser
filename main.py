import mysql.connector

connection = mysql.connector.connect(
    host="sql301.infinityfree.com",
    user="if0_38945782",
    password="Momobady1989",
    database="if0_38945782_badinjetslux"
)

cursor = connection.cursor()
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()

for table in tables:
    print(table)

cursor.close()
connection.close()
