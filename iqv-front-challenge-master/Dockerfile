FROM python:3.8-alpine
EXPOSE 5000
WORKDIR /
COPY Dockerfile /Dockerfile
WORKDIR /code

COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh
COPY requirements.txt .
COPY requirements_min.txt .
COPY requirements_docker.txt .

RUN apk update && \
 apk add --no-cache --virtual .build-deps alpine-sdk libffi-dev gcc musl-dev linux-headers && \
 pip install --no-cache-dir -r requirements_docker.txt && \
 apk del .build-deps

COPY challenge ./challenge

ENTRYPOINT ["entrypoint.sh"]