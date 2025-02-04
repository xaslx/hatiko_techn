## Запуск сервиса

### 1️⃣ Клонирование репозитория
```sh
git clone https://github.com/xaslx/hatiko_techn.git
cd hatiko_techn
```

### 2️⃣ Установка зависимостей
```sh
poetry install
```

### 4️⃣ .env
```
API_TOKEN: нужен для доступа к бекенду
BOT_TOKEN: Telegram токен бота
IMEI_API_SERVICE_TOKEN: можно получить на https://imeicheck.net/developer-api
FASTAPI_PORT: 8000
```


### 5️⃣ Запуск, Остановка, Логи веб приложения и бота
```sh
make app - запуск веб приложения и бота
make app-down - остановка веб приложения и бота
make app-logs - логи веб приложения
make bot-logs - логи бота

```
