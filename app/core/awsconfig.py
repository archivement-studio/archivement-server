import boto3
import json


def s3_connection():
    try:
        file_path = "./app/hidden/aws_access_config.json"
        with open(file_path, 'r') as file:
            data = json.load(file)
            print(data)

        s3 = boto3.client(
            service_name="s3",
            region_name="ap-northeast-2", # 자신이 설정한 bucket region
            aws_access_key_id=data['aws_access_key_id'],
            aws_secret_access_key=data['aws_secret_access_key'],
        )

    except Exception as e:
        print(e)

    else:
        print("s3 bucket connected!")
        return s3
    
s3 = s3_connection()