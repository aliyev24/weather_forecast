# Weather Forecast

- Login and add cities to your list to see weather forecast for them
- Registration and Authentication
- Form

# Requirements

* Docker

# Build with
* Python 3.9
* Django 4.1.5
* Docker
* Postgres
* External API

# Installation

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
