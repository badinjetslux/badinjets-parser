import mysql.connector
import os

# Connessione al database su Hostinger
connection = mysql.connector.connect(
    host="auth-db1579.hstgr.io",
    user="u536233056_badinjetluxapp",
    password="Momobady1989",
    database="u536233056_badinjetluxapp"
)

cursor = connection.cursor()
cursor.execute("SELECT COUNT(*) FROM empty_legs")
result = cursor.fetchone()
print(f"Totale tratte trovate nel DB: {result[0]}")
connection.close()
