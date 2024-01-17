FROM python:3.9-slim-buster
WORKDIR /usr/src/app
COPY flask_app.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "flask_app.py"]