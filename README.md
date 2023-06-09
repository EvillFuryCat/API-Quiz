# API-Quiz

## Описание проекта

Это Веб сервис исполненый на Python3, с применением FastAPI. Подключение базе данных Postgres осуществляется с помощью библиотеки  SqlAlchemy.
В сервисе определен метод, который с помощью POST запроса передает число в сторонний API https://jservice.io/api/random?count= для получения определенного количиства вопросов викторины и записывает полученную информацию в таблицу базы данных. Также, внутри сервиса происходит проверка: если сервис получает дубликат вопроса викторины, отправляет еще запрос для получения уникального значения.

### Пример запроса 
```
{
  "questions_num": 15 
}
``` 
Такой запрос запишет в базу данных 15 уникальных вопросов для викторины.

Благодаря FastAPI можно без труда проверить работоспособность сервиса, выполнив запрос выше перейдя на автоматически сгенерированную документацию swagger `http://0.0.0.0:8000/docs#`

## Установка зависимостей
Установка зависимостей происходит автоматически с помощью docker
Внутри контейнера установится менеджер пакетов poetry, который добавит необходимые библиотеки в docker контейнер

pyproject.toml
```
python = "^3.11"
fastapi = {extras = ["all"], version = "^0.95.2"}
psycopg2-binary = "^2.9.3"
sqlalchemy = "^2.0.13"
requests = "^2.30.0"
black = "^23.3.0"
```


## Сборка Docker образа и запуск сервера

В корне репозитория необходимо выполнить команду

```
docker compose up
```
Начнется сборка Docker образа и запуск двух изолированных контейнеров api сервиса и отдельно базы данных.
Так как я специально поместил в репозиторий файл .env, дополнительных настроек не потребуется, все переменные окружения, явки и пароли передадутся автоматически.
Это демонстрационный проект, в комерческой разработке подобные данные необходимо тщательно прятать от посторонних глаз и, конечно, создавать базу данных с надежными логином и паролем. 


