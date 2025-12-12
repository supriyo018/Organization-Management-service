from fastapi import APIRouter, HTTPException
from app.schemas.admin_schema import AdminLogin
from app.services.auth_service import AuthService

router = APIRouter(prefix="/admin", tags=["Admin"])
service = AuthService()

@router.post("/login")
def admin_login(data: AdminLogin):
    try:
        token = service.login(data.email, data.password)
        return {"access_token": token}
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
