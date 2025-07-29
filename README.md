# Загрузка в Telegram фотографии космоса

Эта программа позволяет автоматически загружать в Telegram-канал фотографии космоса.

### Как установить

Чтобы запускать скрипты, для начала укажите токен вашего бота, NASA API и chatid, создав файл .env.
Формат:
```
TOKEN='abcdef123456'
CHAT_ID='@telegram'
API='123456abcdef'
```


Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Примеры запуска скриптов

Запуск main.py:

```
main.py <directory>
```
Вместо <directory> - директория с фотографиями

Запуск epic_images_download:

```
epic_images_download.py
```

Запуск apod_images_download:

```
apod_images_download.py
```

Запуск spacex_images_download:

```
spacex_images_download.py <id>
```
Вместо <id> - ID Запуска

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).