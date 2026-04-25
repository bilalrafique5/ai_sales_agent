# main.py or ai_analysis.py
from dotenv import load_dotenv
load_dotenv()  # loads variables from .env

from fastapi import FastAPI
from app.routes.lead_routes import router

app = FastAPI(title="AI Sales Research Assistant")

app.include_router(router)