from fastapi import FastAPI
from app.api.v1.endpoints import users, projects

app = FastAPI(title="ModularTerrainManager", version="1.0.0")

# Include Routers
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(items.router, prefix="/items", tags=["Items"])

@app.get("/")
def read_root():
    return {"message": "Welcome to ModularTerrainManager!"}