from flask import Flask, render_template

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/farmers")
def farmersPage():
    return render_template("farmers.html")

@app.get("/service")
def servicePage():
    return render_template("service.html")

@app.get("/contact")
def contactPage():
    return render_template("contact.html")

@app.get("/sk")
def lobby_sk():
    return render_template("Slovak/lobby_sk.html")

@app.get("/nl")
def lobby_nl():
    return render_template("Dutch/lobbydu.html")


if __name__ == "__main__":
    app.run(debug=True)
