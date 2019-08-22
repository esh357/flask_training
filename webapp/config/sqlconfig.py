DB_USER = "root"
DB_PASSWORD = ""
DB_HOST = "127.0.0.1"
DB_PORT = 3306
DB_NAME = "test_training"

REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_DB = 0

DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{db}'

SQLALCHEMY_DATABASE_URI = DATABASE_URI.format(
    user=DB_USER, password=DB_PASSWORD, host=DB_HOST, db=DB_NAME)

REDIS_URL = f"redis://@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"