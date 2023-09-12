FROM python:3.10.8
LABEL authors="changmin.kim"
EXPOSE 8080

WORKDIR /archivementserver
COPY ./manage.py /archivementserver/manage.py

COPY ./requirements.txt /archivementserver/requirements.txt
RUN pip install --upgrade pip && \
    pip install --upgrade pip setuptools && \
    pip install --no-cache-dir --upgrade -r /archivementserver/requirements.txt

COPY ./app /archivementserver/app

ENTRYPOINT ["python", "manage.py", "runserver", "prod"]
