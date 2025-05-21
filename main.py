
import mysql.connector
import os
from datetime import datetime

# Connessione al database Hostinger
connection = mysql.connector.connect(
    host='127.0.0.1',
    user='u536233056_badinjetluxapp',
    password='Momobady1989',
    database='u536233056_badinjetluxapp'
)

cursor = connection.cursor()

try:
    print(f"[{datetime.now()}] Connessione riuscita. Estraendo dati...")

    cursor.execute("SELECT partenza_citta, arrivo_citta, data_partenza FROM empty_legs ORDER BY data_partenza DESC LIMIT 5")
    results = cursor.fetchall()

    for row in results:
        print(f"Da {row[0]} a {row[1]} - Partenza: {row[2]}")

except mysql.connector.Error as err:
    print(f"Errore: {err}")

finally:
    cursor.close()
    connection.close()
