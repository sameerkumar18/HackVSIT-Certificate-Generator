import boto3, uuid
import os

def make_filename(filename):
    extension = ""
    if ".png" in filename:
        extension = ".png"
    elif ".jpg" in filename:
        extension = ".jpg"
    elif ".jpeg" in filename:
        extension = ".jpeg"
    random_name = str(uuid.uuid4())+extension
    return random_name


def s3_upload(file):
    bucket_name = 'meme-it'
    s3 = boto3.client(
        's3',
        aws_access_key_id=os.environ.get('AWS_ACCESS_KEY'),
        aws_secret_access_key=os.environ.get('AWS_SECRET_KEY')
    )
    Bucket = (bucket_name)
    filename = make_filename(file)
    s3.upload_file(file, Bucket, "certi/"+filename)
    return "https://s3.ap-south-1.amazonaws.com/meme-it/certi/"+filename
