from app.core.config.awsconfig import AwsClient

awsClient = AwsClient()

def test_upload_s3():
    s3 = awsClient.s3
    s3.upload_file(
        Filename="test/resources/test.txt",
        Bucket=awsClient.s3_bucket_name,
        Key="test/test.txt"
    )

def test_put_item_dynamodb():
    dynamodb = awsClient.dynamodb
    row = {
        "id":"1",
        "name":"test"
    }
    table = dynamodb.Table("User")
    table.put_item(Item=row)
