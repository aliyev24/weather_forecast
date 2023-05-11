# Weather Forecast
![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=flat-square)
![DjangoRestFramework](https://img.shields.io/badge/-Django%20Rest%20-880808?logo=django&logoColor=white&style=flat-square)
![Django](https://img.shields.io/badge/-Django-092E20?logo=django&logoColor=white&style=flat-square)
![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-3776AB?logo=postgresql&logoColor=white&style=flat-square)
![Docker](https://img.shields.io/badge/-Docker-2496ED?logo=docker&logoColor=white&style=flat-square)

- Login and add cities to your list to see weather forecast for them
- Registration and Authentication

_ _ _ _ _ _ _ _ _ _ _
### Build with
* Python
* Django 4
* Docker
* Postgres
* Weather API
_ _ _ _ _ _ _ _ _ _ _
### Installation

1. Create '.env' file in settings.py root and paste this:

 ```
DEBUG=0
SECRET_KEY=l8g!36r#0t_x*aflo*u^78oh+)*5w-v_@=s65k1li5qr_!*518

POSTGRES_NAME=your_postgres_name
POSTGRES_USER=your_postgres_username
POSTGRES_PASSWORD=your_postgres_password
POSTGRES_HOST=db
POSTGRES_PORT=5432
   ```

2. Create a docker image and run

```
docker-compose up --build
```
