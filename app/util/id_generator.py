import uuid

def dynamo_id_generator():
    id = str(uuid.uuid1())
    return id

def s3_id_generator():
    id = str(uuid.uuid1())
    return id