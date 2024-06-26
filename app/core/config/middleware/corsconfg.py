from fastapi.middleware.cors import CORSMiddleware

origins = [
    'http://localhost:3000',
    'http://127.0.0.1:3000',
    'http://192.9.127.137:3000',
    'http://172.20.10.3:3000',
    'http://172.20.10.13:3000'
]

def set_cors(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app