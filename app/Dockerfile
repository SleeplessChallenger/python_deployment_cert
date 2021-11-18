FROM python:3

WORKDIR /app

EXPOSE 80

ADD . .

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["python3"]
CMD ["wsgi.py"]
