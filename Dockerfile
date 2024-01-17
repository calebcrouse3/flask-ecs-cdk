FROM python:3.9-slim-buster
WORKDIR /usr/src/app
RUN pip install poetry==1.7.1
COPY ./flask_app/flask_app.py .
COPY poetry.lock .
COPY pyproject.toml .
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi
EXPOSE 5000
CMD ["poetry", "run", "python", "flask_app.py"]