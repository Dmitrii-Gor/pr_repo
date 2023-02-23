import requests
from config import token

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def create_folder(self, file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/"
        headers = self.get_headers()
        params = {'path': file_path}
        responce = requests.put(upload_url, headers = headers, params = params)
        return responce.status_code

def Yandex():
    folder = 'testing'
    uploader = YaUploader(token)
    return uploader.create_folder(folder)