import re
from pymongo.database import Database

def slugify(name: str) -> str:
    name = name.lower().strip()
    return re.sub(r"[^a-z0-9]+", "_", name)

def create_tenant_collection(db: Database, collection_name: str):
    if collection_name not in db.list_collection_names():
        db.create_collection(collection_name)
