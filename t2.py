import requests
import os 
import sys


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
            return {
                'Content-Type': 'application/json',
                'Authorization': 'OAuth {}'.format(self.token)
            }

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        href = self._get_upload_link(disk_file_path=os.path.basename(file_path)).get("href", "")
        response = requests.put(href, data=open(os.path.abspath(file_path), 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("File Uploaded")



if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = "/Users/z/Yandex.Disk/Netology/Введение в типы данных и циклы/ответы на проверку.txt"
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)