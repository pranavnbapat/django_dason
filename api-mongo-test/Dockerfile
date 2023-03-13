FROM python:3.9.7

RUN apt-get update && apt-get upgrade -y

RUN pip install --upgrade pip

WORKDIR /var/www/api-mongo-test

#COPY requirements.txt ./var/www/api-mongo-test

COPY . /var/www/api-mongo-test

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8002"]

