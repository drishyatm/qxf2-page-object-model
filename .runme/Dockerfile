FROM python:latest
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT python tests/test_api_example.py