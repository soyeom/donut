FROM python:3.9.0

WORKDIR /home/

RUN echo "nine"

RUN git clone https://github.com/soyeom/donut.git

WORKDIR /home/donut/

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=donut.settings.deploy && python manage.py migrate --settings=donut.settings.deploy && gunicorn donut.wsgi --env DJANGO_SETTINGS_MODULE=donut.settings.deploy --bind 0.0.0.0:8000"]