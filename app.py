from flask import Flask, render_template, request, url_for, redirect
import db

app = Flask(__name__)

@app.route ("/")
def startseite():
    return render_template ("index.html") # Hier den Namen der HTML-Datei angeben, die geladen werden soll.

@app.route ("/verwalten")    
def verwalten():
    return render_template("verwalten.html")

@app.route ("/zeiten")    
def zeiten():
    return render_template("zeiten.html")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=8080, debug=True)