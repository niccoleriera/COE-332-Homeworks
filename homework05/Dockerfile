FROM python:3.9

RUN pip3 install --user flask
RUN pip3 install --user redis

RUN mkdir /data
WORKDIR /data

COPY . /data
ENTRYPOINT ["python"]
CMD ["app.py"]
