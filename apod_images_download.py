import requests
import os
from urllib.parse import urlsplit, unquote, urlparse
import argparse
from dotenv import load_dotenv


load_dotenv()

if not os.path.exists('images'):
    os.makedirs('images')


def apod_images_download(api):
    payload = {'api_key': {api}, 'count': 5}
    response = requests.get('https://api.nasa.gov/planetary/apod', params=payload)
    for num, element in enumerate(response.json()):
        url = element['url']
        img_response = requests.get(url)
        filename = f'images/apod{num}{get_extension(url)[1]}'
        with open(filename, 'wb') as file:
            file.write(img_response.content)


def get_extension(link):
    unquoted = unquote(link)
    parsed_url = urlparse(unquoted)
    path, full_name = os.path.split(parsed_url.path)
    filename, extension = os.path.splitext(full_name)
    return filename, extension


def main():
    API = os.getenv('API')
    apod_images_download(API)


if __name__ == '__main__':
    main()