from app.core.awsconfig import s3,dynamodb

def test_upload_s3():
    s3.upload_file(
        Filename="./app/test/resources/test.txt",
        Bucket="archivement-bucket",
        Key="/test.txt"
    )

def test_put_item_dynamodb():
    row = {
        "id":"1",
        "name":"test"
    }
    table = dynamodb.Table("User")
    table.put_item(Item=row)
