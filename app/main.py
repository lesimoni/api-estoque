from fastapi import FastAPI
from .routes import router

app = FastAPI(title="API Estoque")

app.include_router(router)
