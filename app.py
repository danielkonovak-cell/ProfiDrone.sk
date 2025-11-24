# ✅ import from the 'project' package
from flask import Flask, render_template

app = Flask(__name__)

# --- Main site pages (HTML templates) ---
@app.get("/")
def home():
    return render_template('lobby.html')

if __name__ == '__main__':
    app.run(debug=True)
