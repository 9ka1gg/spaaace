import requests
import os
from urllib.parse import urlsplit, unquote, urlparse
import datetime


if not os.path.exists('images'):
    os.makedirs('images')


def spacex_images_download():
    response = requests.get('https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a')
    urls = response.json()['links']['flickr']['original']
    for num, url in enumerate(urls):
        image_response = requests.get(url)
        filename = f'images/spacex{num}.jpg'
        with open(filename, 'wb') as file:
            file.write(image_response.content)


def apod_images_download():
    payload = {'api_key': 'MkGNWS5AjOhiDRaWVDR6d7asghEhplSjz3dpsDvy', 'count': 5}
    response = requests.get('https://api.nasa.gov/planetary/apod', params=payload)
    for num, element in enumerate(response.json()):
        url = element['url']
        img_response = requests.get(url)
        filename = f'images/apod{num}{get_extension(url)[1]}'
        with open(filename, 'wb') as file:
            file.write(img_response.content)


def epic_images_download():
    payload = {'api_key': 'MkGNWS5AjOhiDRaWVDR6d7asghEhplSjz3dpsDvy', 'count': 5}
    response = requests.get('https://api.nasa.gov/EPIC/api/natural', params=payload)
    response_data = response.json()
    for num, element in enumerate(response_data):
        date = element['date']
        name = element['image']
        date = datetime.datetime.fromisoformat(date).strftime('%Y/%m/%d')
        payload_image = {'api_key': 'MkGNWS5AjOhiDRaWVDR6d7asghEhplSjz3dpsDvy'}
        image = requests.get(f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{name}.png', params=payload_image)
        filename = f'images/epic{num}.png'
        with open(filename, 'wb') as file:
            file.write(image.content)


        
def get_extension(link):
    unquoted = unquote(link)
    parsed_url = urlparse(unquoted)
    path, full_name = os.path.split(parsed_url.path)
    filename, extension = os.path.splitext(full_name)
    return filename, extension
