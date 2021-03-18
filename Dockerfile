FROM python:3.9.0-buster

WORKDIR /srv/mini-backend

COPY ./ .

RUN python3 -m pip install -r requirements.txt

EXPOSE 5000

VOLUME ["/srv/mini-backend/"]

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]