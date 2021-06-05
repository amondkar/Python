FROM python:3
ADD MyApi.py /
ADD Pipfile /
ADD Pipfile.lock /
RUN pip install pipenv
RUN pipenv install --deploy --ignore-pipfile
EXPOSE 8080
CMD ["pipenv","run", "python", "./MyApi.py"]