build:
	@docker build -t flask-app-hello-world .

tar:
	@docker save flask-app-hello-world > image-target/flask-app-hello-world.tar

run:
	@docker run --rm -it -p 5000:5000 flask-app-hello-world

dump-deps:
	@poetry export --without-hashes --format=requirements.txt > flask_app/requirements.txt

synth:
	@cd cdk & poetry run cdk synth