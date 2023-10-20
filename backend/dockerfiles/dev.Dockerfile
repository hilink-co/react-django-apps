FROM python:3.12

WORKDIR /app/backend
RUN apt-get update && apt-get install -y default-mysql-client
COPY requirements.txt /app/backend
RUN pip3 install --upgrade pip -r requirements.txt

# RUN python manage.py makemigrations backend
# RUN python manage.py migrate backend
COPY . /app/backend
EXPOSE 8000