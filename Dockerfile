FROM python:3.10.2
WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt
EXPOSE 8080
CMD [ "python3", "app.py"]