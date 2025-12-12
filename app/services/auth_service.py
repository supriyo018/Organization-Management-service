from app.core.database import admins_collection
from app.core.security import verify_password, create_jwt

class AuthService:

    def login(self, email: str, password: str):
        admin = admins_collection.find_one({"email": email})
        if not admin or not verify_password(password, admin["password"]):
            raise ValueError("Invalid credentials")

        return create_jwt({"admin_id": str(admin["_id"])})
