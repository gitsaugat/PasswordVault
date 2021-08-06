FROM python:3.7-alpine
WORKDIR /code
ENV PYTHONUNBUFFERED=1
RUN apk update \
    && apk add --virtual build-deps python3-dev musl-dev \
    && apk add jpeg-dev zlib-dev  \
    && apk add --no-cache gcc libc-dev git \
    && apk add postgresql-dev autoconf automake libtool nasm\
    && apk add postgresql-client\
    && apk del build-deps \
    && apk add  gdal-dev gdal --update-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing \
    && apk add  geos-dev geos --update-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing \
    && rm -fr /var/cache/apk
COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt 
COPY . .
CMD python manage.py collectstatic --no-input; python manage.py runserver makemigrations; python manage.py migrate; python manage.py runserver 0.0.0.0 8000
