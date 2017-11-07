from flask import Flask, render_template, g
import sqlite3

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/mit")
def mit():
    return render_template('college.html', data=getFromDb("Massachusetts Institute of Technology"))

@app.route("/stanford")
def stanford():
    return render_template('college.html', data=getFromDb("Stanford"))

@app.route("/carnegiemellon")
def carnegiemellon():
    return render_template('college.html', data=getFromDb("Carnegie Mellon"))

@app.route("/berkeley")
def berkeley():
    return render_template('college.html', data=getFromDb("University of California-Berkeley"))

@app.route("/georgiatech")
def georgiatech():
    return render_template('college.html', data=getFromDb("Georgia Institute of Technology"))

@app.route("/cornell")
def cornell():
    return render_template('college.html', data=getFromDb("Cornell"))

@app.route("/michigan")
def michigan():
    return render_template('college.html', data=getFromDb("University of Michigan"))

@app.route("/compare")
def compare():
    return render_template("compare.html", data=getAllFromDb())


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
    for s in query_db('SELECT * FROM schools'):
        if (s['name'] == name):
            return s

def getAllFromDb():
    # Get all, alphabetically
    return query_db('SELECT * FROM schools ORDER BY name ASC')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
