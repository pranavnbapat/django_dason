FROM python:3.9.7

RUN apt-get update && apt-get upgrade -y

RUN pip install --upgrade pip

WORKDIR /var/www/apicore

#COPY requirements.txt ./var/www/apicore

COPY . /var/www/apicore

RUN pip install --no-cache-dir -r requirements.txt

#EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]
