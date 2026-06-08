from flask import Flask, render_template, request, url_for, redirect
import sqlite3
import db

app = Flask(__name__)

@app.route ("/")
def startseite():
    return render_template ("index.html") # Hier den Namen der HTML-Datei angeben, die geladen werden soll.

@app.route("/verwalten", methods=["GET", "POST"])
def verwalten():

    if request.method == "POST":

        name = request.form["name"]
        vorname = request.form["vorname"]
        jahrgang = request.form["jahrgang"]
        klasse = request.form["klasse"]
        zeit = request.form["zeit"]

        conn = sqlite3.connect("Läufer-Schüler.db")
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO Laeufer
            (name, vorname, klasse, jahrgang, zeit)
            VALUES (?, ?, ?, ?, ?)
        """, (name, vorname, klasse, jahrgang, zeit))

        conn.commit()
        conn.close()

        return redirect("/verwalten")

    return render_template("verwalten.html")

@app.route("/zeiten")
def zeiten():

    conn = sqlite3.connect("Läufer-Schüler.db")
    conn.row_factory = sqlite3.Row

    cur = conn.cursor()

    daten = cur.execute(
        "SELECT * FROM Laeufer"
    ).fetchall()

    conn.close()

    return render_template(
        "zeiten.html",
        daten=daten
    )

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=8080, debug=True)