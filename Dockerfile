FROM ubuntu:latest
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN apt-get -y install libmysqlclient-dev
RUN pip3 install -r requirements.txt
COPY . /app
ENTRYPOINT [ "python3" ]
CMD ["main.py"]