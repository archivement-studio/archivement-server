from pydantic import BaseModel

class PostPoster(BaseModel):
    name: str
    image_number: str
    x_position: int
    client_image_width: int
    client_line_gap: int
