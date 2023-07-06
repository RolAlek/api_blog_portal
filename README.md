# api_yatube_final

## Описание
### API-приложение блога реализованное на Django REST Framework.
Приложение позволяет оплучать и создовать публикации и коментариеи. Также реализованна возможность тегирования публикаций по категироиям (управление категориями доступно администратору блога) и возможность подписываться на интересующих авторов. В сервисе реализованна авторизация по JWT-токену. Неавторизованным пользователям досутпна возможность просмотра контента, кроме подписок пользователя(только для пользователя отправившего запрос). Возможность создавать публикации и коментарии к ним доступна только авторизованным пользователям. Возможность управления контентом(публикации и комментарии) доступна только авторам контента.

## Установка и запуск
> Обратите внимание: указанные команды приведены для Unix-систем(MacOS и Linux). Команды для Windows могут отличаться!

Клонируйте git-репозиторий выполнив команду в терминале:

```
git clone https://github.com/RolAlek/api_final_yatube.git
```

перейдите в каталог с проектом:

```
cd api_fianl_yatube
```

Создайте и активируйте виртуальное окружение:

```
python3 -m venv <название_окружения>
```
```
source venv/bin/activate
```

Обновите менеджер пакетов pip и примените зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Примените миграции:

```
python3 manage.py migrate
```

Запустите проект:

```
python3 manage.py runserver
```

## Примеры некоторых запросов

Полуение публикаций

GET-запрос к эндпоинту `http://127.0.0.1:8000/api/v1/posts/`

```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```

Создание публикации

POST-запрос к эндпоинту `http://127.0.0.1:8000/api/v1/posts/`:
```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
В случае успеха сервер вернет ответ с кодом `200`:
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}

#### Примеры неудачных запросов:
Ответ с кодом `400` - неправильно составлен запрос:
```
{
  "text": [
    "Обязательное поле."
  ]
}
```
Ответ с кодом `401` - запрос выполнен неавторизованным пользователем:
```
{
  "detail": "Учетные данные не были предоставлены."
}
```