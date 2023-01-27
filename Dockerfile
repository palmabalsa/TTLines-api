# pull official base image
FROM python:3.10-slim-buster
EXPOSE 8000

# ENV AWS_REGION sydney
# Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONUNBUFFERED 1

# set work directory eg: /usr/src/app
WORKDIR /app

# install dependencies
RUN pip install --upgrade pip
# COPY ./requirements.txt .
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# copy all project files from working dir(.)  into this currrent dir (.)
COPY . /app/

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]