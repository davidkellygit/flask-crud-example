FROM python:3.8-alpine
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
RUN sudo apt -y install libmysqlclient-dev
COPY . /app
ENTRYPOINT [ "python" ]
CMD ["main.py"]