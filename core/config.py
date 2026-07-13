import os

class Config:
    SECRET_KEY = 'kunci_rahasia_uas_cloud'
    STORAGE_DIR = os.path.join(os.getcwd(), 'simulasi_s3_bucket')

os.makedirs(Config.STORAGE_DIR, exist_ok=True)