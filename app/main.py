from fastapi import FastAPI

from app.core.awsconfig import s3, dynamodb

def create_app():
    app = FastAPI()
    return app
