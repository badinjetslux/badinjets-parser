
import mysql.connector

connection = mysql.connector.connect(
    host="aws.connect.psdb.io",
    user="railway_user",
    password="LA_TUA_PASSWORD",  # Sostituisci con la password reale
    database="badinjetslux",
    ssl_ca="cacert.pem"
)

cursor = connection.cursor()
cursor.execute("SHOW TABLES;")
for table in cursor.fetchall():
    print(table)

cursor.close()
connection.close()
