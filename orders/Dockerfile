FROM python:3-alpine

COPY app /app_new

WORKDIR /app_new

RUN  pip install -r requirments.txt

ENTRYPOINT ["python", "orders.py"]


