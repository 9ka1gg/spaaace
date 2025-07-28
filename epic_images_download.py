import requests
import os
import datetime


if not os.path.exists('images'):
    os.makedirs('images')


def epic_images_download(api):
    payload = {'api_key': api, 'count': 5}
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


def main():
    api_key = 'MkGNWS5AjOhiDRaWVDR6d7asghEhplSjz3dpsDvy'
    epic_images_download(api_key)


if __name__ == '__main__':
    main()