docker-build:
	sudo docker-compose --env-file .env build 

docker-up:
	sudo docker-compose --env-file .env up -d

docker-down:
	sudo docker-compose down
