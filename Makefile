docker-build:
	sudo docker-compose --env-file .env build --no-cache

docker-up:
	sudo docker-compose --env-file .env up

docker-down:
	sudo docker-compose down