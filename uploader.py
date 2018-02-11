import boto3,uuid

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
        aws_access_key_id='AKIAJIHVDGPBNYMSDCCA',
        aws_secret_access_key='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'
    )
    Bucket = (bucket_name)
    filename = make_filename(file)
    s3.upload_file(file, Bucket, "certi/"+filename)
    return "https://s3.ap-south-1.amazonaws.com/meme-it/certi/"+filename
