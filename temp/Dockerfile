FROM python:2
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
ENV MONGO_HOST=docker.for.mac.host.internal
CMD [ "python", "src/app.py"]
#CMD [ "FLASK_APP=main.py flask run" ]