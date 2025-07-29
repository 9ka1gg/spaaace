import telegram
from telegram.error import NetworkError
import argparse
from random import shuffle
import os
from time import sleep
from dotenv import load_dotenv

load_dotenv()
bot = telegram.Bot(token=os.getenv('TOKEN'))


def auto_publish(directory):
        cooldown = 14400
        tree = list(os.walk(directory))
        images_list = tree[0][2]
        while True:
            try:
                for element in images_list:
                    print(element)
                    bot.send_photo(chat_id='@spaceteee', photo=open(f'{directory}/{element}', 'rb'))
                    sleep(cooldown)
                shuffle(images_list)
            except NetworkError:
                print('Ошибка сети, повтор через 20 секунд')
                sleep(20)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('directory', help='Директория с фотками')
    args = parser.parse_args()
    auto_publish(args.directory)


if __name__ == '__main__':
    main()