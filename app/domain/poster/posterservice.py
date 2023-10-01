from app.domain.poster.dto.post_poster import PostPoster
from app.util.poster_generator import transform_stretch
from app.core.http.response.http_response import *
from app.util.pil2byte import pil2byte
from app.core.config.awsconfig import AwsClient
from app.util.id_generator import s3_id_generator, dynamo_id_generator
from app.util.qr_util import qr_generator
from datetime import datetime
from PIL import Image
import os


class PosterService:
    def addPoster(self, post_poster: PostPoster):
        image_number = post_poster.image_number
        x_position = post_poster.x_position
        name = post_poster.name
        client_image_width = post_poster.client_image_width
        client_line_gap = post_poster.client_line_gap

        img = transform_stretch(image_number,x_position,client_image_width,client_line_gap)

        img_pil = Image.fromarray(img)
        img_byte_arr = pil2byte(img_pil)

        aws_client = AwsClient()
        s3 = aws_client.s3
        poster_image_path = AwsClient.s3_poster_images_path
        poster_id = s3_id_generator()
        key = poster_image_path + poster_id + '.png'

        s3.put_object(
            Body=img_byte_arr, 
            Bucket=aws_client.s3_bucket_name, 
            Key = key
        )

        dynamodb = aws_client.dynamodb
        now = datetime.utcnow().isoformat()
        row = {
            "id":dynamo_id_generator(),
            "name":name,
            "path":key,
            "createdAt":now,
            "updatedAt":now,
            "deletedAt":None,
        }
        table = dynamodb.Table("Poster")
        table.put_item(Item=row)

        date = datetime.fromisoformat(now).date().isoformat()

        address = os.environ['server_url']#"http://192.9.127.137:8080"
        image_url = aws_client.s3_bucket_url+"/"+key
        qr_url = address+"/images/?image_url="+image_url
        print(qr_url)
        qr_data = qr_generator(qr_url)
        
        response_201['image_url'] = image_url
        response_201['qr_data'] = qr_data
        response_201['name'] = name
        response_201['date'] = date

        return response_201