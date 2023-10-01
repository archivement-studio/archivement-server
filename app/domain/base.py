from app.domain.poster import postercontroller
from app.domain.image import imagecontroller

routers = [
    imagecontroller.router,
    postercontroller.router
]