class Config:
    ALLOW_INSTALLATION = True
    ALLOW_LOGIN = True
    ALLOW_REGISTRATION = True
    ALLOW_PUBLISHING_NEW_PACKAGES = True
    ALLOW_PUBLISHING_NEW_RELEASES = True
    # Not recommended, still in early stages and is missing multiple features
    ENABLE_CONSOLE = False
    REQUIRE_ADMIN_TO_INSTALL = False
    REQUIRE_ADMIN_TO_PUBLISH = True
    REQUIRE_LOGIN_TO_INSTALL = False

    SECRET_KEY = 'changeme'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///birdy.db'
