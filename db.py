import sqlite3

def verbindung_herstellen():
    return sqlite3.connect("Läufer-Schüler.db")

def schüler_hinzufügen(name, Vorname, klasse, sportlehrer,zeit):
    verbindung = verbindung_herstellen()
    cursor = verbindung.cursor()
    cursor.execute("""
    INSERT INTO Laeufer (name, vorname, klasse, sportlehrer, zeit)
    VALUES (?, ?, ?, ?,?)
    """, (name, Vorname, klasse, sportlehrer, zeit))
    verbindung.commit()
    verbindung.close()


def schüler_aktualisieren(schüler_id, name, Vorname, klasse, sportlehrer,zeit):
    verbindung = verbindung_herstellen()
    cursor = verbindung.cursor()
    cursor.execute("""
    UPDATE Laeufer
    SET name = ?, vorname = ?, klasse = ?, sportlehrer = ?, zeit = ?
    WHERE schüler_id = ?
    """, (name, Vorname, klasse, sportlehrer, zeit, schüler_id))
    verbindung.commit()
    verbindung.close()


def schüler_löschen(schüler_id):
    verbindung = verbindung_herstellen()
    cursor = verbindung.cursor()
    cursor.execute("""
    DELETE FROM Laeufer
    WHERE schüler_id = ?
    """, (schüler_id,))
    verbindung.commit()
    verbindung.close()


def schüler_anzeigen():
    verbindung = verbindung_herstellen()
    cursor = verbindung.cursor()
    cursor.execute("""
    SELECT * FROM Laeufer
    """)
    schüler = cursor.fetchall()
    verbindung.close()
    return schüler


def schüler_suchen(name):
    verbindung = verbindung_herstellen()
    cursor = verbindung.cursor()
    cursor.execute("""
    SELECT * FROM Laeufer
    WHERE name LIKE ?
    """, ('%' + name + '%',))
    schüler = cursor.fetchall()
    verbindung.close()
    return schüler


def schüler_nach_zeit_suchen(zeit):
    verbindung = verbindung_herstellen()
    cursor = verbindung.cursor()
    cursor.execute("""
    SELECT * FROM Laeufer
    WHERE zeit <= ?
    """, (zeit,))
    schüler = cursor.fetchall()
    verbindung.close()
    return schüler


verbindung = verbindung_herstellen()
cursor = verbindung.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Laeufer (
    schüler_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    vorname TEXT,
    klasse TEXT,
    sportlehrer TEXT,
    zeit FLOAT,
    jahrgang TEXT
               )
               """)

verbindung.commit() # speichert Änderungen
verbindung.close() # schließt die Verbindung