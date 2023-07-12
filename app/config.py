class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql:///pet_adopt'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_RECORD_QUERIES = True
    SECRET_KEY = 'secret'
    DEBUG = True
    FLASK_APP = 'app'
    