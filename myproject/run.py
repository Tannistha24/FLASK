from myproject import app, db

with app.app_context():
    db.create_all()  # This ensures MySQL tables are created

if __name__ == '__main__':
    app.run(debug=True)
