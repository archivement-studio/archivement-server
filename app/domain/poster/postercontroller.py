from fastapi import APIRouter
from app.domain.poster.dto.post_poster import *
from app.core.version.app_version import api_version
# from app.core.http.response.http_response import *
# from app.util.poster_generator import transform_stretch
from app.domain.poster.posterservice import PosterService

posterService = PosterService();

router = APIRouter(
    prefix=api_version+"/posters",
    tags=["posters"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", tags=["posters"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]

@router.post("/", tags=["posters"],status_code=201)
async def add_poster(post_poster: PostPoster):
    response_201 = posterService.addPoster(post_poster=post_poster)
    return response_201