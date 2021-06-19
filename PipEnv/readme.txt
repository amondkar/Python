pipenv install flask
pipenv install flask_restful
pipenv lock


docker build -t pipenv-flask .
docker run --name flask-api -p 8081:8080 -it pipenv-flask 
docker tag pipenv-flask flask-api-pipenv
docker tag pipenv-flask amondkar/pipenv-flask
docker login
docker image push amondkar/pipenv-flask
