from app import create_app

app = create_app()

if __name__ == '__travisci__':
    app.run(debug=True)
