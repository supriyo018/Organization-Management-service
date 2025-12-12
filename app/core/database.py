from pymongo import MongoClient
from app.core.config import MONGO_URI, MASTER_DB_NAME

client = MongoClient(MONGO_URI)
master_db = client[MASTER_DB_NAME]

organizations_collection = master_db["organizations"]
admins_collection = master_db["admins"]
