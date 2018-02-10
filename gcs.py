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



# from google.cloud import storage
# import google.auth
# from google.oauth2 import service_account
# from google.cloud.storage import Blob
# from thug_life.settings import STATIC_URL
#
# CLIENT_SECRETS_FILE = "thuglife/memify/thugmeme-afcbf5f91ac6.json"
# # imagePath="sample.jpg"
#
#
# def authorized_client(cred_file_path, project_name):
#     credentials = service_account.Credentials.from_service_account_file(
#         cred_file_path)
#     client = storage.Client(credentials=credentials, project=project_name)
#     return client
#
#
# def get_bucket(client, bucket_name):
#     bkt = client.get_bucket(bucket_name)
#     return bkt
#
#
# def upload_public_file(client, bkt, file_name):
#     # file_name in Blob constructor is the file name you want to have on GCS
#     blob = Blob(file_name, bkt)
#     # file_name in open function is the one that actually sits on your hard drive
#     with open(file_name, 'rb') as my_file:
#         blob.upload_from_file(my_file)
#     # after uploading the blob, we set it to public, so that it's accessible with a simple link
#     blob.make_public(client)
#
#
# def send_file_to_google_cloud(file_name,project_name,bucket_name):
#
#     cred_file_path = CLIENT_SECRETS_FILE
#     client = authorized_client(cred_file_path=cred_file_path,project_name=project_name)
#     bkt = get_bucket(client, bucket_name=bucket_name)
#     try:
#         upload_public_file(client, bkt, file_name=file_name)
#         return "https://storage.cloud.google.com/thugmeme/" + file_name
#     except:
#         try:
#             file_name = "1"+file_name
#             upload_public_file(client, bkt, file_name=file_name)
#             return "https://storage.cloud.google.com/thugmeme/"+file_name
#         except:
#             print("Couldn't upload file to GCS")
#             return "unsuccessful"
#
