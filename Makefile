build:
	@docker build -t flask-hello-world .

run:
	@docker run --rm -it -p 5000:5000 flask-hello-world

push:
	@aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 202571202047.dkr.ecr.us-east-2.amazonaws.com
	@docker tag flask-hello-world:latest 202571202047.dkr.ecr.us-east-2.amazonaws.com/flask-hello-world:latest
	@docker push 202571202047.dkr.ecr.us-east-2.amazonaws.com/flask-hello-world:latest