from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/mit")
def mit():
    return render_template('college.html', school="Massachusetts Institute of Technology")

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



if __name__ == "__main__":
    app.run()
