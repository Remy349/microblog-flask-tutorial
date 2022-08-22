import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "microblog.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Sending errors by email
    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = int(os.environ.get("MAIL_PORT") or 25)
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS") is not None
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    ADMINS = ["youremail@example.com"]
    # Paginations for posts
    POSTS_PER_PAGE = 5
    # List of supported languages to translate
    LANGUAGES = ["en", "es"]
    # Microsoft translator API key, if you wanna translate posts as well (Optional)
    MS_TRANSLATOR_KEY = os.environ.get("MS_TRANSLATOR_KEY")
