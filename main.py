import mysql.connector

connection = mysql.connector.connect(
    host="srv123.main-hosting.eu",  # <-- metti qui l'host corretto che vedi su Hostinger
    user="u536233056_badinjetluxapp",
    password="Momobady1989",
    database="u536233056_badinjetluxapp")

cursor = connection.cursor()
cursor.execute("SHOW TABLES")

for table in cursor:
    print(table)

cursor.close()
connection.close()
