class Config:
    ALLOW_LOGIN = True
    ALLOW_REGISTRATION = True
    ALLOW_PUBLISHING = True
    REQUIRE_ADMIN_TO_PUBLISH = True
    REQUIRE_LOGIN_TO_INSTALL = False

    SECRET_KEY = 'changeme'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///birdy.db'