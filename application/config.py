import os


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True

    db_user = os.environ.get('DB_USER')
    db_password = os.environ.get('DB_PASSWORD')
    db_host = os.environ.get('DB_HOST')
    db_schema = os.environ.get('DB_SCHEMA')

     # mysql
    SQLALCHEMY_DATABASE_URI = f'mysql://{db_user}:{db_password}@{db_host}/{db_schema}'


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