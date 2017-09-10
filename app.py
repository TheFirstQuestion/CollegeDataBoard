from flask import Flask, render_template, g
import sqlite3

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/mit")
def mit():
    return render_template('college.html', school="Massachusetts Institute of Technology", data=getFromDb("Massachusetts Institute of Technology"))

@app.route("/stanford")
def stanford():
    return render_template('college.html', school="Stanford")

@app.route("/carnegiemellon")
def carnegiemellon():
    return render_template('college.html', school="Carnegie Mellon")

@app.route("/caltech")
def caltech():
    return render_template('college.html', school="California Institute of Technology")

@app.route("/berkeley")
def berkeley():
    return render_template('college.html', school="UC Berkeley")

@app.route("/georgiatech")
def georgiatech():
    return render_template('college.html',school="Georgia Institute of Technology")

@app.route("/penn")
def penn():
    return render_template('college.html', school="University of Pennsylvania")

@app.route("/brown")
def brown():
    return render_template('college.html', school="Brown University")

@app.route("/harvard")
def harvard():
    return render_template('college.html', school="Harvard")

@app.route("/compare")
def compare():
    return render_template("compare.html")


# Database stuff
# http://flask.pocoo.org/docs/0.12/patterns/sqlite3/
DATABASE = 'collegedataboard.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def getFromDb(name):
    for user in query_db('SELECT * FROM schools'):
        if (user['name'] == name):
            return user


if __name__ == "__main__":
    app.run()
