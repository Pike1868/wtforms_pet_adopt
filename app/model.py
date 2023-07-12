from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/img/35934"


def connect_db(app):
    """Connect to database."""
    db.app = app

# Models (schema) will go below


class Pet(db.Model):
    """Pet table, will have id[PK], name, species, photo_url, age, notes, and available columns"""

    __tablename__ = 'pets'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.String(50),
                     nullable=False)
    species = db.Column(db.String(50),
                        nullable=False)
    photo_url = db.Column(db.String(500), nullable=False)
    age = db.Column(db.Integer)
    notes = db.Column(db.String(500))
    available = db.Column(db.Boolean, nullable=True, default=True)
