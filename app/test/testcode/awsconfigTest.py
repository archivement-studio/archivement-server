from app.core.awsconfig import s3

def test_upload_s3():
    s3.upload_file(
        Filename="./app/test/resources/test.txt",
        Bucket="archivement-bucket",
        Key="/test.txt"
    )