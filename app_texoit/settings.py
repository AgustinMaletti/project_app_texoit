import os
from pathlib import Path
# from dotenv import load_dotenv

# load_dotenv()
BASE_PATH = Path(__file__).parent.resolve()
DATA_FILE = BASE_PATH.joinpath("data", "movielist.csv")
DATA_FILE2 = BASE_PATH.joinpath("data", "winners.csv")

"/home/baltasar/data/WORLD/DEV/TESTES/project_app_texoit/app_texoit/data"
SQLALCHEMY_DATABASE_URI = 'sqlite:///scrapyboy.db'

DB_H2_PATH = BASE_PATH.joinpath('db', 'h2', 'bin', 'h2-2.1.214').__str__()

# DB_SQLITE3 =  BASE_PATH.joinpath('db', 'db_app_texoit.db')

SQLALCHEMY_DATABASE_URI = 'sqlite:///db_app_texoit.db'
MONGO_CONFIG_FILE_PATH = BASE_PATH.joinpath("mongo_db.json")
# DEBUG = False 
# DATABASE
# the environ.get is for deploy config
# os.environ.get('DATABASE_URL')
# SQLALCHEMY_DATABASE_URI =

# MONGO_URI = "mongodb://localhost:27017/myDatabase"
MONGO_URI = "mongodb+srv://scrapyboy:calixto136@cluster0.hlcc2.mongodb.net/scrapyWebApp"

SECRET_KEY = os.environ.get('SECRET_KEY')
PRESERVE_CONTEXT_ON_EXCEPTION = False
# Cross site request forgery protection
WTF_CSRF_SECRET_KEY = os.environ.get('SECRET_KEY')
TESTING = False
SECRET_KEY = os.urandom(32)
# app.config['SECRET_KEY'] = SECRET_KEY

# MAIL
MAIL_SERVER = 'smtp.zoho.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_DEBUG = True


#MAIL_DEFAULT_SENDER = 'consultoria@scrapyboy.com.br'
#MAIL_USERNAME = 'consultoria@scrapyboy.com.br'
MAIL_DEFAULT_SENDER = 'bot@scrapyboy.com.br'
MAIL_USERNAME = 'bot@scrapyboy.com.br'
MAIL_PASSWORD = 'Bot136_!'
# RECAPTCHA
RECAPTCHA_SITE_KEY = '6Leo5aEUAAAAAGQDda_75637ffi9_RouoJSGQjVk'
RECAPTCHA_SECRET_KEY = '6Leo5aEUAAAAAIXi7GPre4Ynv-zpQ3zlhFYSAiV3'
RECAPTCHA_ENABLED = False
RECAPTCHA_THEME = "light"
RECAPTCHA_TYPE = "image"
RECAPTCHA_RTABINDEX = 10

# EXPLAIN_TEMPLATE_LOADING=True
# EXPLAIN_STATIC_LOADING=True



