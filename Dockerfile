FROM python

EXPOSE 8000
WORKDIR /app
CMD gunicorn --bind 0.0.0.0:8000 wsgi
COPY app /app
RUN pip install -r /app/requirements.txt
