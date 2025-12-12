from pydantic import BaseModel, EmailStr

class OrganizationCreate(BaseModel):
    organization_name: str
    email: EmailStr
    password: str

class OrganizationGet(BaseModel):
    organization_name: str

class OrganizationUpdate(BaseModel):
    old_name: str
    new_name: str
