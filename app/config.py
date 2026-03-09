import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "sales_agent"

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")