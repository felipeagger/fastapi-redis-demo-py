FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN mkdir -p /home/py/app

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]
