from python

copy app.py /app.py
copy requirements.txt /requirements.txt

run pip install -r /requirements.txt
expose 5000
cmd python /app.py
