from fastapi import APIRouter, HTTPException, Depends
from app.schemas.organization_schema import (
    OrganizationCreate,
    OrganizationGet,
    OrganizationUpdate
)
from app.services.organization_service import OrganizationService
from app.core.security import get_current_admin

router = APIRouter(prefix="/org", tags=["Organization"])
service = OrganizationService()

@router.post("/create")
def create_org(data: OrganizationCreate):
    try:
        return service.create_organization(data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/get")
def get_org(data: OrganizationGet):
    try:
        return service.get_organization(data.organization_name)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.put("/update")
def update_org(
    data: OrganizationUpdate,
    admin_id: str = Depends(get_current_admin)
):
    try:
        service.update_organization(data.old_name, data.new_name, admin_id)
        return {"message": "Organization updated successfully"}
    except PermissionError as e:
        raise HTTPException(status_code=403, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/delete")
def delete_org(
    organization_name: str,
    admin_id: str = Depends(get_current_admin)
):
    try:
        service.delete_organization(organization_name, admin_id)
        return {"message": "Organization deleted successfully"}
    except PermissionError as e:
        raise HTTPException(status_code=403, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
