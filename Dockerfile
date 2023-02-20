FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8001
CMD gunicorn -w 4 -b 0.0.0.0:8001 --timeout 3600 "app:app"
