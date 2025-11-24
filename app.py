from project import create_app   # ✅ import from the 'project' package

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
