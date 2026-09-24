from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Nikodem"

@app.route("/o-nas")
def onas():
    return "Nazywam się nikodem naperty, lubię jeść pizzę i nie jestem winny kartosowi pizzy."

@app.route("/kontakt")
def kont():
    return "eeeee, nie mam zbytnio kontaktów"

@app.route("/regulamin")
def reg():
    return "Tutaj 0 prostych zasad."

if __name__ == "__main__":
    app.run(debug=True)