from fastapi import FastAPI
from app.routes.lead_routes import router

app = FastAPI(title="AI Sales Research Assistant")

app.include_router(router)