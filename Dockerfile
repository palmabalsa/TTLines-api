# pull official base image
FROM python:3.10-slim-buster

# set work directory eg: /usr/src/app
WORKDIR /app

# set env vars:

# ENV AWS_REGION sydney
# Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
# COPY ./requirements.txt .
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . .

# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
