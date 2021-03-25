<h1 align="center">Welcome to mqtt-ia-concept 👋</h1>
<p>
  <img alt="Ubuntu" src="https://img.shields.io/ubuntu/v/ubuntu-wallpapers/bionic" />
  <img alt="Python" src="https://img.shields.io/pypi/pyversions/Django" />
  <a href="https://github.com/jeffersonamoriim/mqtt-ia-concept#readme" target="_blank">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" />
  </a>
</p>

### 🏠 [Homepage](https://github.com/jeffersonamoriim/mqtt-ia-concept#readme)

> Mqtt-ia-concept it's an project thats concepts an architecture idea of devices sendind data with mqtt to rabbitmq and create linear regression events that provides predictions to this devices

## Install

> Change .env-example to .env to all services run properly

```sh
  docker-compose up -d
  sudo su
  setup.sh
```

# Linux privileges

> Also you need do grant all privileges to your unix user

```sh
    sudo chown -R $user .
```

## Usage (with .venv activated)

```sh
  python predictor/manage.py migrate
  python predictor/manage.py createsuperuser --email example@example.com.br --username admin
  python predictor/manage.py runserver

```

> After this go to http://localhost:8000/devices and create two devices

## Publish and consume data from rabbitmq

```sh
  python mqtt/publisher.py
  python mqtt/consumer.py
```

## Services

* **rabbitmq:** http://127.0.0.1:15672 (user: rabbitmq | password: rabbitmq)
* **postgres:** 127.0.0.1:5432 (user: root | password: postgres)

## Author

👤 **Jefferson Amorim**

* Github: [@jeffersonamoriim](https://github.com/jeffersonamoriim)

## 📝 License

Copyright © 2021 [Jefferson Amorim](https://github.com/jeffersonamoriim).
