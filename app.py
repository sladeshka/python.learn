import os
from flask import Flask
from flask_migrate import Migrate
from models import db
import psycopg2

app: Flask = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://learn:password@127.0.0.1:5460/learn'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)
app.config['DEBUG'] = True

db.init_app(app)
migrate = Migrate(app, db)

with app.app_context():
    if os.path.exists('./db/backup.sql'):
        with app.open_resource('./db/backup.sql') as f:
            conn = psycopg2.connect("dbname=learn user=learn password=password port=5460")
            cur = conn.cursor()
            cur.execute(f.read().decode('utf-8'))
            conn.commit()
            cur.close()
            conn.close()
    db.create_all()

from routes import *

if __name__ == '__main__':
    app.run(debug=True)
