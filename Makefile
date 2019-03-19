up:
	docker-compose up --build

build:
	sudo docker-compose run web django-admin startproject cheat .

createsuperuser:
	docker-compose exec web python manage.py createsuperuser


update_games:
	docker-compose exec web python manage.py runscript update_games; \

migrate:
	docker-compose exec web python manage.py makemigrations; \
	docker-compose exec web python manage.py migrate;

down:
	docker-compose down

