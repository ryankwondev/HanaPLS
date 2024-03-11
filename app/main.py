from fastapi import FastAPI
from app.login import get_personal_code

app = FastAPI(title="HanaPLS API")
