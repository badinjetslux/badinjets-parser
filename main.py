import mysql.connector

connection = mysql.connector.connect(
    host="mysql.hostinger.com",  # ⚠️ Sostituisci con l'host corretto se diverso (es:  `srvxxx.main-hosting.eu`)
    user="u536233056_badinjetluxapp",
    password="Momobady1989",
    database="u536233056_badinjetluxapp"
)

cursor = connection.cursor()
cursor.execute("SHOW TABLES")

for table in cursor:
    print(table)

cursor.close()
connection.close()
