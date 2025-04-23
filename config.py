import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'super-secret-watchman-key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'entry.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
