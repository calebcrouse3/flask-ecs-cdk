# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /usr/src/app

RUN pip install poetry==1.7.1

# Copy the current directory contents into the container at /usr/src/app
COPY ./flask_app/ ./flask_app/
COPY poetry.lock .
COPY pyproject.toml .

# Install any needed packages specified in requirements.txt
RUN poetry install --no-dev

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["poetry", "run", "python", "flask_app/flask_app.py"]