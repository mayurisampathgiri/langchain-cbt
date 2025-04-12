from fastapi import FastAPI
from backend.cbt_router import router as cbt_router

app = FastAPI(title="CBT Test API")
app.include_router(cbt_router)