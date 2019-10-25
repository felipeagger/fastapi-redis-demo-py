GIT_CURRENT_BRANCH := ${shell git symbolic-ref --short HEAD}

.PHONY: help clean test run

.DEFAULT: help

help:
	@echo "make clean:"
	@echo "       Removes all pyc, pyo and __pycache__"
	@echo ""
	@echo "make docker:"
	@echo "       Run app with docker and docker-compose"
	@echo ""
	@echo "make dockerdown:"
	@echo "       Remove app from docker with docker-compose down"
	@echo ""
	@echo "make setup"
	@echo "       Install dependencies"
	@echo "       set virtualenv on this path"
	@echo ""
	@echo "make test:"
	@echo "       Run tests with pytest(necessary Redis ON)"
	@echo ""
	@echo "make rundev:"
	@echo "       Run the web application(necessary Redis ON)"
	@echo ""

clean:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . | grep -E "__pycache__|.pytest_cache|.pyc|.DS_Store$$" | xargs rm -rf

docker:
	@echo "---- Building & Up Container ----"
	@docker-compose down
	@docker-compose build	
	@docker-compose up -d
	@sleep 5
	@echo "---- EndPoints ----"
	@echo "---- Fast API - http://127.0.0.1:8000/docs ----"

dockerdown:
	@docker-compose down

setup:
	@echo "---- Setting Enviroment ----"
	@virtualenv env
	@. env/bin/activate
	@echo "---- Installing Python dependencies ----"
	@pip3 install -r requirements.txt --upgrade

test:
	@pytest --verbose --disable-pytest-warnings --color=yes tests/

rundev:
	uvicorn main:app --reload