FROM python

RUN mkdir /app
WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt && \
    pip install -e .