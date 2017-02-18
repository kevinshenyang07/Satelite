from flask import Flask
import model

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///satelite.db'
db = SQLAlchemy(app)
