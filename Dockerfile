FROM tensorflow/tensorflow:2.0.0-py3 as dev

ENV FLASK_APP src/app.py
ENV FLASK_DEBUG 1
WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
ENTRYPOINT [ "flask", "run" ]
CMD ["--host=0.0.0.0" , "--port=80"]

FROM dev
ENTRYPOINT [ "uwsgi" ]
CMD ["--http=:80", "--processes=1", "--threads=1", "--wsgi-file=src/app.py", "--callable=app"]
