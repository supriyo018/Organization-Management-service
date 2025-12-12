from datetime import timedelta

MONGO_URI = "mongodb://localhost:27017"
MASTER_DB_NAME = "master_db"

JWT_SECRET_KEY = "supriyo_backend"
JWT_ALGORITHM = "HS256"
JWT_EXPIRATION_TIME = timedelta(hours=1)
