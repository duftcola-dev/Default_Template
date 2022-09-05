FROM python:3.8.10 

WORKDIR /.
COPY . . 
RUN pip install -r ./requirements/requirements.txt  --upgrade pip
RUN export FLASK_APP=app
EXPOSE 3000
CMD ["gunicorn","-w 4","-b 0.0.0.0:3000","--reload","-e FLASK_DEBUG=development","main:app"]
