FROM python:3.10.1 as base

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . /app/

# FROM base AS test
# CMD [ "python3", "-m", "unittest", "discover", "tests", "*_test.py"]

# FROM test AS build
# CMD ["python3", "-m", "app.hello"]
