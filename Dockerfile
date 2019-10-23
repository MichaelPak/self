FROM python:3.6

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV production

COPY ./requirements.txt /code/requirements.txt
RUN pip install --upgrade pip && \
    pip install -r /code/requirements.txt
COPY ./docker-entrypoint.sh /code/docker-entrypoint.sh

COPY src /code/
WORKDIR /code/

RUN useradd wagtail
RUN chown -R wagtail /code
USER wagtail

EXPOSE 8000
ENTRYPOINT ["docker-entrypoint.sh"]
