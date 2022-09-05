# Configuration Handler 
    Flask default template.

# Description :
    Configuration and cli handler module.
    Its main function is to keep track of the processes made by the cli and display
    the available options to build projects.
    This project is originally conceived to be used in other projects with Flask.
## Author:
    Robin Viera
## Email:
    robinviera@hotmail.com
## Version : 1.0.0
## Stable : No
## Requirements:
    - Python 3.8>=
    - Python 3.8 venv
    - Docker [optional]
    - Docker-compose [optional]
## Platform :
    Linux Ubuntu Focal

## DESCRIPTION :

    Default template for quick development of microservices and small applications

## DEVELOPMENT

    For development purposes this projects uses make 
    though in the near future a proper cli in python will be implemented.

    Some of the test run using a virtual environment. In the future all features will be run 
    in a docker container.

    sintaxis : make <command>

    COMMANDS:
        install: Creates a virtual environment and installs all the deppendencies required
                for local development.

        database: Creates and initializes a local  sqlite3 database for testing and development.

           
        console: Logs into sqlite3 shell

        develop_local: Runs the guicorn test server using the created virtual enviroment

        develop: Runs a docker compose file using the docker-compose .env config file.

        test: Runs automated test and generated a coverage file using the virtual enviroment installation.

        down: Kill any running gunicorn process.

        list: Generates a list with the installed deppendencies as well as generating the 
              requirements.txt files.

        docker: Creates a docker images with our app and runs it.

        start: Starts the created docker image
        
        stops: Stops the created docker image

        flush: Deletes all images and containers created.
	

