FROM python:3.7.0
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT pytest -k api