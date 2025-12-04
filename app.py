from flask import Flask, render_template

app = Flask(__name__)

# ============================================================
#                    ENGLISH PAGES
# ============================================================

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

@app.get("/login")
def loginPage():
    return render_template("Login.html")

@app.get("/register")
def registerPage():
    return render_template("register.html")

@app.get("/users")
def usersPage():
    return render_template("users.html")



# ============================================================
#                    SLOVAK PAGES
# ============================================================

@app.get("/sk")
def lobby_sk():
    return render_template("Slovak/lobby_sk.html")

@app.get("/sk/farmers")
def farmers_sk():
    return render_template("Slovak/farmers_sk.html")

@app.get("/sk/service")
def service_sk():
    return render_template("Slovak/service_sk.html")

@app.get("/sk/contact")
def contact_sk():
    return render_template("Slovak/Contact_sk.html")

@app.get("/sk/login")
def login_sk():
    return render_template("Slovak/LogIn_sk.html")

@app.get("/sk/register")
def register_sk():
    return render_template("Slovak/register_sk.html")

@app.get("/sk/users")
def users_sk():
    return render_template("Slovak/users_sk.html")



# ============================================================
#                    DUTCH PAGES
# ============================================================

@app.get("/nl")
def lobby_nl():
    return render_template("Dutch/lobbydu.html")

@app.get("/nl/farmers")
def farmers_nl():
    return render_template("Dutch/Farmersdu.html")

@app.get("/nl/service")
def service_nl():
    return render_template("Dutch/servicedu.html")

@app.get("/nl/contact")
def contact_nl():
    return render_template("Dutch/Contactdu.html")

@app.get("/nl/login")
def login_nl():
    return render_template("Dutch/LogIndu.html")

@app.get("/nl/register")
def register_nl():
    return render_template("Dutch/registerdu.html")

@app.get("/nl/users")
def users_nl():
    return render_template("Dutch/usersdu.html")



# ============================================================

if __name__ == "__main__":
    app.run(debug=True)
