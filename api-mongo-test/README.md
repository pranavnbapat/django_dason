### api-mongo-test
release version 0.0.1


### Local Setup

Create venv
```
python3 -m venv ./venv
```
Activate venv 
```
source venv/scripts/activate
```
Install requirements
```
pip install -r requirements.txt
```
Test API is running locally
```
uvicorn app.main:app
```
You can navigate to `localhost:8000/docs` from your browser to check 
FastAPI is running ok.

Build Image
```
docker build -t api-mongo .
```
Create network (if communicating with another container)
```
docker network create mongo_db
```
Bring up Container
```
docker compose up --build -d
```
To get inside the container open a new terminal window and run
```
docker exec -it api_mongo bash
```