DC = docker compose
LOGS = docker logs
ENV = --env-file .env
APP_FILE = docker_compose/fastapi.yaml
APP_CONTAINER = main-app
BOT_FILE = docker_compose/bot.yaml
BOT_CONTAINER = bot


.PHONY: app
app:
	${DC} -f ${APP_FILE} -f ${BOT_FILE} ${ENV} up --build -d


.PHONY: app-logs
app-logs:
	${LOGS} ${APP_CONTAINER} -f


.PHONY: app-down
app-down:
	${DC} -f $(APP_FILE) -f ${BOT_FILE} down


.PHONY: bot
bot:
	${DC} -f ${BOT_FILE} ${ENV} up --build -d

.PHONY: bot-down
bot-down:
	${DC} -f ${BOT_FILE} ${ENV} down

.PHONY: bot-logs
bot-logs:
	${LOGS} ${BOT_CONTAINER} -f
