import sqlite3

def verbindung_herstellen():
    return sqlite3.connect("Läufer Schüler.db")

def produkte_hinzufügen(name, Vorname, klasse, sportlehrer,zeit):
    verbindung = verbindung_herstellen()
    cursor = verbindung.cursor()
    cursor.execute("""
    INSERT INTO einkaufsliste (name, vorname, klasse, sportlehrer, zeit)
    VALUES (?, ?, ?, ?)
    """, (name, Vorname, klasse, sportlehrer, zeit))
    verbindung.commit()
    verbindung.close()



verbindung = verbindung_herstellen()
cursor = verbindung.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS einkaufsliste (
    schüler_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    vorname TEXT,
    klasse TEXT,
    sportlehrer TEXT,
    zeit FLOAT
               )
               """)