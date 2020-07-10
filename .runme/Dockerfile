FROM python:3.8.0
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT python tests/test_example_form.py