from flask import Flask, render_template, request, url_for, redirect
import sqlite3
import db

app = Flask(__name__)

@app.route ("/")
def startseite():
    return render_template ("index.html") # Hier den Namen der HTML-Datei angeben, die geladen werden soll.

@app.route("/verwalten", methods=["GET", "POST"])
def verwalten():

    conn = sqlite3.connect("Läufer-Schüler.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    if request.method == "POST":

        if "hinzufuegen" in request.form:
            name = request.form["name"]
            vorname = request.form["vorname"]
            jahrgang = request.form["jahrgang"]
            klasse = request.form["klasse"]
            zeit = request.form["zeit"]

            cur.execute("""
                INSERT INTO Laeufer
                (name, vorname, klasse, jahrgang, zeit)
                VALUES (?, ?, ?, ?, ?)
            """, (name, vorname, klasse, jahrgang, zeit))

        if "loeschen" in request.form:
            schueler_id = request.form["schueler_id"]
            cur.execute("""
                DELETE FROM Laeufer
                WHERE rowid = ?
            """, (schueler_id,))
        conn.commit()
        conn.close()

        return redirect("/verwalten")

    schueler = cur.execute("""
        SELECT rowid, * FROM Laeufer
        ORDER BY jahrgang, klasse, name
    """).fetchall()
    conn.close()

    return render_template("verwalten.html", schueler=schueler)

@app.route("/zeiten")
def zeiten():
    conn = sqlite3.connect("Läufer-Schüler.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    daten = cur.execute("""
        SELECT * FROM Laeufer
        ORDER BY jahrgang, klasse, name
    """).fetchall()

    conn.close()

    return render_template("zeiten.html", daten=daten)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=8080, debug=True)

def datenbank_pruefen():
    conn = sqlite3.connect("Läufer-Schüler.db")
    cur = conn.cursor()

    try:
        cur.execute("ALTER TABLE Laeufer ADD COLUMN jahrgang TEXT")
    except sqlite3.OperationalError:
        pass

    try:
        cur.execute("ALTER TABLE Laeufer ADD COLUMN zeit TEXT")
    except sqlite3.OperationalError:
        pass

    conn.commit()
    conn.close()


datenbank_pruefen()