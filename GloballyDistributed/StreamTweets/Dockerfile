FROM python:2
COPY requirements.txt /
RUN pip install -r requirements.txt
COPY stream.py /
CMD python stream.py