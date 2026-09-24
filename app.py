from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Nikodem"

@app.route("/o-nas")
def onas():
    return "Nazywam się nikodem naperty, lubię jeść pizzę i nie jestem winny kartosowi pizzy."


if __name__ == "__main__":
    app.run(debug=True)