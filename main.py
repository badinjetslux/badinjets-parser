import mysql.connector
import requests
import time
import re
import os

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = "@badinjetslux"

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

API_URL = f"https://api.telegram.org/bot{TOKEN}/getUpdates"

def extract_data(text):
    match = re.search(r"(?P<from>[\w\s]+)\s*→\s*(?P<to>[\w\s]+).*?Date[:\-]?\s*(?P<date>\d{1,2}/\d{1,2}/\d{4}).*?Jet[:\-]?\s*(?P<jet>[\w\s\-]+).*?Seats[:\-]?\s*(?P<seats>\d+)", text, re.DOTALL)
    if match:
        return {
            "partenza_citta": match.group("from").strip(),
            "arrivo_citta": match.group("to").strip(),
            "data_partenza": match.group("date").replace("/", "-"),
            "jet_model": match.group("jet").strip(),
            "posti": int(match.group("seats"))
        }
    return None

def save_to_db(data, link):
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASS,
            database=DB_NAME
        )
        cursor = conn.cursor()
        sql = """
            INSERT INTO empty_legs (
                partenza_citta, arrivo_citta, data_partenza,
                jet_model, posti, link_telegram, created_at
            ) VALUES (%s, %s, %s, %s, %s, %s, NOW())
        """
        values = (
            data["partenza_citta"], data["arrivo_citta"], data["data_partenza"],
            data["jet_model"], data["posti"], link
        )
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        print("Offerta salvata:", data)
    except Exception as e:
        print("Errore salvataggio:", e)

def run():
    last_id = None
    while True:
        res = requests.get(API_URL)
        if res.status_code == 200:
            for msg in res.json()["result"]:
                if "channel_post" in msg:
                    post = msg["channel_post"]
                    if post["chat"]["username"] == CHANNEL[1:] and post["message_id"] != last_id:
                        text = post.get("text", "")
                        link = f"https://t.me/{CHANNEL[1:]}/{post['message_id']}"
                        data = extract_data(text)
                        if data:
                            save_to_db(data, link)
                            last_id = post["message_id"]
        time.sleep(60)

if __name__ == "__main__":
    run()
