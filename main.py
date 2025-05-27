import mysql.connector

# Connessione al database aggiornato
connection = mysql.connector.connect(
    host="sql301.infinityfree.com",
    user="if0_38945782",
    password="Momobady1989",
    database="if0_38945782_badinjetslux"
)

# Esegui una semplice query di test
cursor = connection.cursor()
cursor.execute("SELECT COUNT(*) FROM empty_legs")
result = cursor.fetchone()
print("Numero di voli empty leg disponibili:", result[0])

cursor.close()
connection.close()
