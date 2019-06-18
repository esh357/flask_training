DB_USER = "root"
DB_PASSWORD = "root"
DB_HOST = "localhost"
DB_PORT = 3306
DB_NAME = "testprog"

DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{db}'

SQLALCHEMY_DATABASE_URI = DATABASE_URI.format(
    user=DB_USER, password=DB_PASSWORD, host=DB_HOST, db=DB_NAME)
