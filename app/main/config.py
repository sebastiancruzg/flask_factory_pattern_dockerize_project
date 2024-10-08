import os
import dataclasses

basedir = os.path.abspath(os.path.dirname(__file__))


@dataclasses.dataclass
class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "my_precious_secret_key")
    DEBUG = False


@dataclasses.dataclass
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_secret_key')
    DB_USER = os.getenv('MYSQL_USER')
    DB_PASSWORD = os.getenv('MYSQL_PASSWORD')
    DB_NAME = os.getenv('MYSQL_DATABASE')
    DB_HOST = os.getenv('MYSQL_HOST')
    DB_PORT = os.getenv('DBPORT')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://%s:%s@%s:%s/%s' % (
        DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'ttndevelop@gmail.com'
    MAIL_PASSWORD = 'ghnsejxvfzauidog'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_size': 1,
        'pool_recycle': 1,
        'pool_timeout': 60,
        'pool_pre_ping': True
    }


@dataclasses.dataclass
class ProductionConfig(Config):
    DEBUG = False
    DB_USER = os.getenv("MYSQL_USER")
    DB_PASSWORD = os.getenv("MYSQL_PASSWORD")
    DB_NAME = os.getenv("MYSQL_DATABASE")
    DB_HOST = os.getenv("MYSQL_HOST")
    DB_PORT = os.getenv("DBPORT")
    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://" + f"{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )


config_by_name = dict(
    dev=DevelopmentConfig,
    local=DevelopmentConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
