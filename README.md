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
DEBUG=True # вывод подробных ошибок
DATABASE_URL=sqlite:///./db.sqlite3 # подключение БД
SECRET_KEY=django-insecure-r!i0s78w3q_mao&k^u)w1a2_!%we3g=ied5ked7$(855&hjr(g # ключ безопасности, можете использовать этот для разработки
ALLOWED_HOSTS=* # разрешенные хосты для запуска
ADMINSITE=True # подключать админку
DJANGO_SUPERUSER_USERNAME=admin # имя админа
DJANGO_SUPERUSER_EMAIL=admin@mnft.company # почта админа
DJANGO_SUPERUSER_PASSWORD=password # пароль админа
```

## Запуск
```
docker-compose -f docker-compose.yml up -d --build
```
После успешного запуска, сервер будет доступен по адресам:
http://localhost:8000/admin/ - админка, для упрощения работы с тестовыми данными
http://localhost:8000/graphql/ - оболочка для запросов GraphQL
