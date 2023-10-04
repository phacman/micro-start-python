FROM python:3.11-alpine3.18
RUN pip3 install --root-user-action=ignore python-dotenv
WORKDIR /app
COPY .env .
COPY main.py .
CMD [ "python", "./main.py" ]