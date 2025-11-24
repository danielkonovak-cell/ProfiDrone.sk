# ✅ import from the 'project' package
from flask import Flask, render_template

app = Flask(__name__)

# --- Main site pages (HTML templates) ---
@app.get('/')
def testing():
    return render_template('base.html')
    #return render_template('lobby.html')

if __name__ == '__main__':
    app.run(debug=True)


# Too overloaded - menej contentu, zlednodusit!!!!