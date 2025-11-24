# ✅ import from the 'project' package
from flask import Flask

app = Flask(__name__)

# --- Main site pages (HTML templates) ---
@app.route("/")
def home():
    return "Hello there"
    #return render_template('lobby.html')

if __name__ == '__main__':
    app.run()
