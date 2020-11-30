from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Spot(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.Text())
