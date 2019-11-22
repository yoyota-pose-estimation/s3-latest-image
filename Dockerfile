FROM tensorflow/tensorflow:2.0.0-py3 as dev
WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN apt install -y libpcre3 libpcre3-dev
RUN pip install uwsgi
COPY . .

WORKDIR /usr/src/app/src
ENTRYPOINT [ "uwsgi" ]
