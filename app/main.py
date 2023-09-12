from fastapi import FastAPI

from app.core.awsconfig import s3

def create_app():
    app = FastAPI()
    return app
