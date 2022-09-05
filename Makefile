install:

	python -m venv venv
	. venv/bin/activate ; pip install -r  ./requirements/requirements.txt
#. venv/bin/activate ; pip install -e .
	. venv/bin/activate ; pip list


database : 

	- sqlite3 ./app/database/test-db.db  ".read ./app/database/test-init.sql"

console:

	- sqlite3 ./app/database/test-db.db

develop_local:
	
	. venv/bin/activate ; export FLASK_APP=app 
	. venv/bin/activate ; gunicorn -w 4 -b 0.0.0.0:3000 --reload -e FLASK_DEBUG=development main:app

develop:
	docker-compose --env-file .env up

test:

	. venv/bin/activate ; coverage run -m pytest
	. venv/bin/activate ; coverage report 
	. venv/bin/activate ; coverage report > ./doc/report/.report
	. venv/bin/activate ; coverage html -d ./doc/html/
	google-chrome ./doc/html/index.html

docker_test:

	docker build -t duftcola/app_template:latest .
	docker run -d -p 3000:3000 -e CI=true --name app_template_container  duftcola/app_template
	docker exec -it app_template_container pytest tests/
	docker stop app_template_container
	docker rm app_template_container

down:

#shut down gunicorn process 
	pkill -f gunicorn

list:

	. venv/bin/activate; pip freeze > ./requirements/requirements.txt 
	. venv/bin/activate; pip list > ./requirements/list.txt

docker:

	docker build -t duftcola/app_template:latest .
	docker run  -p 3000:3000 --name app_template duftcola/app_template
	docker logs app_template

start:

	docker start app_template

stop:

	docker stop app_template

flush:

	- docker stop app_template
	- docker rm app_template
	- docker rmi duftcola/app_template:latest
	