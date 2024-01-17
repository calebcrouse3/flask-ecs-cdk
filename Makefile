build:
	@docker build -t flask-app flask_app

run:
	@docker run --rm -it -p 5000:5000 flask-app

dump-deps:
	@poetry export --without-hashes --format=requirements.txt > flask_app/requirements.txt
