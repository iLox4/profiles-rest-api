docker rm django-docker
docker rmi -f profiles-rest-api-django-web:latest
docker compose up --build