from fastapi import FastAPI
from app.routes.organization_routes import router as org_router
from app.routes.auth_routes import router as auth_router

app = FastAPI(title="Organization Management Service")

app.include_router(org_router)
app.include_router(auth_router)

@app.get("/")
def health_check():
    return {"status": "running"}
