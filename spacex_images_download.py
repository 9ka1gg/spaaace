import requests
import os
import argparse


if not os.path.exists('images'):
    os.makedirs('images')


def spacex_images_download(id):
    response = requests.get(f'https://api.spacexdata.com/v5/launches/{id}')
    urls = response.json()['links']['flickr']['original']
    for num, url in enumerate(urls):
        image_response = requests.get(url)
        filename = f'images/spacex{num}.jpg'
        with open(filename, 'wb') as file:
            file.write(image_response.content)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('id', help='ID запуска')
    args = parser.parse_args()
    spacex_images_download(args.id)


if __name__ == '__main__':
    main()