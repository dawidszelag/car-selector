docker-build:
	docker-compose --env-file .env build

docker-up:
	docker-compose --env-file .env up -d

docker-down:
	docker-compose down

docker-restart:
	docker-compose restart

docker-logs:
	docker-compose logs -f