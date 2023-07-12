from flask import Flask
from .model import db, connect_db
from .config import Config
from .routes import main
from flask_debugtoolbar import DebugToolbarExtension


def create_app(config_name):
    """Creates the flask app context"""
    app = Flask(__name__)
    app.config.from_object(f"app.config.{config_name}")

    toolbar = DebugToolbarExtension(app)

    connect_db(app)
    db.init_app(app)

    app.register_blueprint(main)
   
    with app.app_context():
        from . import routes
        from . import model
        model.db.create_all()

    return app

app = create_app('Config')