FROM python:2

EXPOSE 8000
WORKDIR /app
copy requirements.txt /requirements.txt
#RUN pip install ConfigParser
RUN pip install -r /requirements.txt
CMD  gunicorn --bind 0.0.0.0:8000 wsgi
#CMD python app.py 
COPY login /app
