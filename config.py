import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'postgres'
    SQLALCHEMY_DATABASE_URI = "postgres://yqojsfoghzhdub:26f4738955bc176171b1408e90dc635c4732e2547f7d6528d5cb0a395570417a@ec2-54-156-53-71.compute-1.amazonaws.com:5432/dfqpraab0bs1kr///books_store"


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
