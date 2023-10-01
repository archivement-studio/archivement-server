from fastapi import APIRouter,Request
from fastapi.templating import Jinja2Templates

templatees = Jinja2Templates(directory="resources/static/templates")

router = APIRouter(
    prefix="/images",
    tags=["images"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", tags=["images"])
async def read_users(request:Request, image_url:str):
    print(image_url)
    context:dict = {"request":request, 'image_url':image_url}
    return templatees.TemplateResponse("poster.html",context=context)