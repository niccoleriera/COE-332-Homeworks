FROM python:3.9

RUN pip3 install --user flask
RUN pip3 install --user redis

RUN mkdir /data
WORKDIR /data
ENV FLASK_APP=/app/app.py

COPY . /data
ENTRYPOINT ["python"]
CMD ["app.py"]
