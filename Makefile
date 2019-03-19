
run:
	python3 manage.py runserver;

migrate:
	python3 manage.py makemigrations; \
	python3 manage.py migrate;

flush:
	python3 manage.py flush;

createsuperuser:
	python3 manage.py createsuperuser;

update_games:
	python3 manage.py runscript update_games
