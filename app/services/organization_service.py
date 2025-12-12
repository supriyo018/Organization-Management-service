from datetime import datetime
from bson import ObjectId
from app.core.database import master_db, organizations_collection, admins_collection
from app.core.security import hash_password
from app.utils.tenant_manager import slugify, create_tenant_collection

class OrganizationService:

    def create_organization(self, data):
        if organizations_collection.find_one({"name": data.organization_name}):
            raise ValueError("Organization already exists")

        slug = slugify(data.organization_name)
        collection_name = f"org_{slug}"

        create_tenant_collection(master_db, collection_name)

        admin_id = admins_collection.insert_one({
            "email": data.email,
            "password": hash_password(data.password),
            "created_at": datetime.utcnow()
        }).inserted_id

        org = {
            "name": data.organization_name,
            "slug": slug,
            "collection_name": collection_name,
            "admin_id": admin_id,
            "created_at": datetime.utcnow()
        }

        organizations_collection.insert_one(org)
        return org

    def get_organization(self, name: str):
        org = organizations_collection.find_one({"name": name})
        if not org:
            raise ValueError("Organization not found")
        return org

    def update_organization(self, old_name: str, new_name: str, admin_id: str):
        org = organizations_collection.find_one({"name": old_name})
        if not org:
            raise ValueError("Organization not found")

        if str(org["admin_id"]) != admin_id:
            raise PermissionError("Unauthorized")

        if organizations_collection.find_one({"name": new_name}):
            raise ValueError("Organization name already exists")

        new_slug = slugify(new_name)
        new_collection = f"org_{new_slug}"

        create_tenant_collection(master_db, new_collection)

        old_data = list(master_db[org["collection_name"]].find())
        if old_data:
            master_db[new_collection].insert_many(old_data)

        master_db.drop_collection(org["collection_name"])

        organizations_collection.update_one(
            {"_id": org["_id"]},
            {"$set": {
                "name": new_name,
                "slug": new_slug,
                "collection_name": new_collection
            }}
        )

    def delete_organization(self, name: str, admin_id: str):
        org = organizations_collection.find_one({"name": name})
        if not org:
            raise ValueError("Organization not found")

        if str(org["admin_id"]) != admin_id:
            raise PermissionError("Unauthorized")

        master_db.drop_collection(org["collection_name"])
        organizations_collection.delete_one({"_id": org["_id"]})
        admins_collection.delete_one({"_id": ObjectId(admin_id)})
