FROM python:3.10.2
WORKDIR .
RUN pip install -r requirements.txt
EXPOSE 8080
CMD [ "python3", "./app.py"]