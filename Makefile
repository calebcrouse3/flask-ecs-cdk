build:
	@docker build -t flask-app-hello-world .

tar:
	@docker save flask-app-hello-world > cdk/docker-image.tar

run:
	@docker run --rm -it -p 5000:5000 flask-app-hello-world