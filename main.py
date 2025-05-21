
import os
import re
import time
import logging
import mysql.connector
from datetime import datetime
from telethon.sync import TelegramClient
from telethon.tl.types import MessageEntityTextUrl

# === CONFIGURAZIONE ===
API_ID = 'YOUR_API_ID'
API_HASH = 'YOUR_API_HASH'
BOT_TOKEN = 'YOUR_BOT_TOKEN'
CHANNEL = 'badinjetslux'  # senza @

DB_HOST = '127.0.0.1'
DB_USER = 'u536233056_badinjetluxapp'
DB_PASS = 'Momobady1989'
DB_NAME = 'u536233056_badinjetluxapp'

# === LOG ===
logging.basicConfig(level=logging.INFO)
log = logging.getLogger("BadinJetsParser")

# === CONNESSIONE DB ===
def db_connect():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME
    )

# === PARSING POST ===
def parse_post(text):
    try:
        data = {}
        # Parsing base
        data["partenza_citta"] = re.search(r"From: (.+?)\n", text).group(1).strip()
        data["arrivo_citta"] = re.search(r"To: (.+?)\n", text).group(1).strip()
        data["data_partenza"] = re.search(r"Date: (.+?)\n", text).group(1).strip()
        data["jet_model"] = re.search(r"Jet: (.+?)\n", text).group(1).strip()
        data["posti"] = int(re.search(r"Seats: (\d+)", text).group(1))
        data["prezzo"] = float(re.search(r"Price: €([\d,.]+)", text).group(1).replace(",", ""))
        return data
    except Exception as e:
        log.warning(f"Parsing fallito: {e}")
        return None

# === SALVATAGGIO DB ===
def save_to_db(data, link):
    conn = db_connect()
    cur = conn.cursor()

    sql = (
        "INSERT INTO empty_legs "
        "(partenza_citta, arrivo_citta, data_partenza, jet_model, posti, prezzo, link_telegram, created_at) "
        "VALUES (%s, %s, %s, %s, %s, %s, %s, NOW())"
    )
    cur.execute(sql, (
        data["partenza_citta"],
        data["arrivo_citta"],
        datetime.strptime(data["data_partenza"], "%d/%m/%Y").date(),
        data["jet_model"],
        data["posti"],
        data["prezzo"],
        link
    ))
    conn.commit()
    conn.close()

# === MAIN FUNCTION ===
def run():
    with TelegramClient('session_name', API_ID, API_HASH).start(bot_token=BOT_TOKEN) as client:
        for message in client.iter_messages(CHANNEL, limit=20):
            if message.text and "From:" in message.text:
                data = parse_post(message.text)
                if data:
                    save_to_db(data, f"https://t.me/{CHANNEL}/{message.id}")
                    log.info(f"Inserito: {data['partenza_citta']} → {data['arrivo_citta']}")

if __name__ == "__main__":
    run()
