# GLOBALS 

user:=duftcola
production:=cv_flask
development:=development
testing:=testing
tag:=latest

#------------------------------------------------

# Build local venv 
# Installs required deppendencies
install: venv clients requirements list
	echo "Installation completed"

# Create a venv
venv:
	python -m venv venv

# Clients necessary for databases like Mysql
clients:
	. venv/bin/activate ; sudo apt-get install python3-dev default-libmysqlclient-dev build-essential

# Install requirements
requirements:
	. venv/bin/activate ; pip install -r  ./project/requirements/requirements.txt --upgrade pip

# List deppendencies and requirements
list:
	. venv/bin/activate ; pip freeze > project/requirements/requirements.txt
	. venv/bin/activate ; pip list > project/requirements/list.txt

#--------------------------------------------------------------------------------

# Launch application in development mode using the venv
develop:
	. venv/bin/activate ;\
	export FLASK_APP=main;\
	gunicorn -w 4 -b 0.0.0.0:5000 --reload -e ENV=development main:app

# Launch application in production mode using the venv
production:
	. venv/bin/activate ;\
	export FLASK_APP=main;\
	gunicorn -w 4 -b 0.0.0.0:5000 --reload -e ENV=production main:app

# Launch the application in test mode using the venv
test:
	. venv/bin/activate ; export ENV=testing; coverage run -m pytest
	. venv/bin/activate ; coverage report -m
	. venv/bin/activate ; coverage report -m > project/doc/report.txt
	. venv/bin/activate ; coverage html -d ./project/doc/html/
	google-chrome ./project/doc/html/index.html

#----------------------------------------------------------------------------------------

# Launches the application in development mode using docker
develop_docker:
	docker run -td -p 3000:3000 --name $(user)_$(development)  $(user)/$(development)

# Launches the application in test mode using docker
test_docker:
	docker run -d -p 3000:3000 -e CI=true --name $(user)_$(testing)  $(user)/$(testing)
	docker exec -it $(user)_$(testing) pytest app/tests/
	docker stop $(user)_$(testing)
	docker rm $(user)_$(testing)

# Launches the application in production mode using docker
production_docker:
	docker run -td -p 3000:3000 --name $(user)_$(production)  $(user)/$(production)

#------------------------------------------------------------------------------------------

# Stop containers
# Forces shut down on gunicorn
stop:
	- docker stop $(user)_$(production)
	- docker stop $(user)_$(development)
	- docker stop $(user)_$(testing)
	- pkill -f gunicorn

# Delete all images and containers
flush:
	- docker stop $(user)_$(development)
	- docker stop $(user)_$(testing)
	- docker stop $(user)_$(production)

	- docker rm $(user)_$(production)
	- docker rm $(user)_$(development)
	- docker rm $(user)_$(testing)

	- docker rmi $(user)/$(production):$(tag)
	- docker rmi $(user)/$(development):$(tag)
	- docker rmi $(user)/$(testing):$(tag)
	
#---------------------------------------------------------------------------------------

# Start containers already built
start_production:
	docker start $(user)_$(production)

start_develop:
	docker start $(user)_$(development)

start_testing:
	docker start $(user)_$(testing)

#----------------------------------------------------------------------------------------

# Builts images and containers
# - develop image
# - production image
# - test image
build: build_production build_develop build_test

	echo 'Images built'
	docker images

build_production: 
	echo 'building $(user)/$(production):$(tag)'
	mv docker/production/.dockerignore .
	mv docker/production/dockerfile .
	docker build -t $(user)/$(production):$(tag) .
	mv .dockerignore docker/production/
	mv dockerfile docker/production/
 
build_develop: 
	echo 'building $(user)/$(development):$(tag)'
	mv docker/development/.dockerignore .
	mv docker/development/dockerfile .
	docker build -t $(user)/$(development):$(tag) .
	mv .dockerignore docker/development/
	mv dockerfile docker/development/

build_test: 
	echo 'building $(user)/$(testing):$(tag)'
	mv docker/testing/.dockerignore .
	mv docker/testing/dockerfile .
	docker build -t $(user)/$(testing):$(tag) .
	mv .dockerignore docker/testing/
	mv dockerfile docker/testing/

#------------------------------------------------------------------------------------------------------

# Creates your database from an init file
init_database:
	- sqlite3 ./project/database/my_database.db  ".read ./project/database/init.sql"
# Creates a database for testing puposes
init_test_database:
	- sqlite3 ./project/database/test-db.db  ".read ./project/database/test-init.sql"	

console:
	- sqlite3 ./project/database/my_database.db

test_console:
	- sqlite3 ./project/database/test-db.db
	

	





