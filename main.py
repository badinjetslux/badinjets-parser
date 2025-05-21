import mysql.connector
from datetime import datetime
import pytz

# Connessione al database su Hostinger
connection = mysql.connector.connect(
    host='srv1222.hstgr.io',  # ← Sostituiscilo se il tuo host MySQL è diverso
    user='u536233056_badinjetluxapp',
    password='Momobady1989',
    database='u536233056_badinjetluxapp'
)

cursor = connection.cursor()

# Esempio di query per vedere se funziona
cursor.execute("SELECT COUNT(*) FROM empty_legs")
result = cursor.fetchone()
print(f"Numero di voli trovati: {result[0]}")

cursor.close()
connection.close()
