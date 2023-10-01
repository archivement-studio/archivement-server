from fastapi import FastAPI
from app.core.config.middleware.corsconfg import set_cors
from app.domain.base import routers
import os

def create_app():
    app = FastAPI()
    if os.environ['server_status'] == "dev":
        app = set_cors(app)
    for router in routers:
        app.include_router(router)
    
    return app
