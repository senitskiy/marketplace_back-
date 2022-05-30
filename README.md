# Установка

## Подготвительные работы

Для разворачивания backend необходим docker и docker-compose. Инструкции: [docker](https://docs.docker.com/engine/install/) и [docker-compose](https://docs.docker.com/compose/install/).

## Клонирование репозитория

```
git clone https://github.com/M-NFT/marketplace_back
cd marketplace_back
```

## Создание файла окружения

Перед установкой необходимо в корне создать .env файл. Пример:
```
DEBUG=True
DATABASE_URL=sqlite:///./db.sqlite3
SECRET_KEY=django-insecure-r!i0s78w3q_mao&k^u)w1a2_!%we3g=ied5ked7$(855&hjr(g
ALLOWED_HOSTS=*
ADMINSITE=True
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@mnft.company
DJANGO_SUPERUSER_PASSWORD=password
```

## Запуск
```
docker-compose -f docker-compose.yml up -d --build
```