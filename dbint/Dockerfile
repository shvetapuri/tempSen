FROM python:2
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV MONGO_HOST=host.docker.internal
EXPOSE 5002
CMD [ "python", "src/app.py"]
#CMD [ "FLASK_APP=main.py flask run" ]
