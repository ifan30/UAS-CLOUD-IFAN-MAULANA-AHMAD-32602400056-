import os
from core.config import Config

class S3SimulationService:
    @staticmethod
    def save_cv_object(file_name, path_txt_s3, data):
        cv_content = f"""=====================================
CONTEN OBJECT BUCKET: bucket-jasa-cv-lokal
PATH KEY: {path_txt_s3}
=====================================
Nama Lengkap: {data['nama']}
Email       : {data['email']}
Nomor HP    : {data['hp']}
Pendidikan  : {data['pendidikan']}
Tema Desain : {data['tema']}
====================================="""
        
        local_file_path = os.path.join(Config.STORAGE_DIR, file_name)
        with open(local_file_path, 'w', encoding='utf-8') as f:
            f.write(cv_content)

    @staticmethod
    def read_cv_object(local_filename):
        local_file_path = os.path.join(Config.Config.STORAGE_DIR, local_filename) if hasattr(Config, 'Config') else os.path.join(Config.STORAGE_DIR, local_filename)
        if os.path.exists(local_file_path):
            with open(local_file_path, 'r', encoding='utf-8') as f:
                return f.read()
        return None

    @staticmethod
    def delete_cv_object(local_filename):
        local_file_path = os.path.join(Config.STORAGE_DIR, local_filename)
        if os.path.exists(local_file_path):
            os.remove(local_file_path)