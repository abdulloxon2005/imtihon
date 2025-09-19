import uvicorn
from fastapi import FastAPI

from app.api import api_retsept


app = FastAPI()
app.include_router(api_retsept.router)

uvicorn.run(app)