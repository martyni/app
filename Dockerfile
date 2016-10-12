FROM python

EXPOSE 8000
WORKDIR /app
copy requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
CMD gunicorn --bind 0.0.0.0:8000 wsgi
#CMD python app.py 
COPY app /app
RUN rm -f /app/basic_app.sqlite
