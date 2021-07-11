FROM python:3.9.5-buster
MAINTAINER Yogesh K
ENV MONGO_DB_USERNAME=admin \
    MONGO_DB_PWD=password

RUN mkdir -p /home/pyapp
RUN pip3 install pymongo

COPY py_mongo.py /home/pyapp
COPY wait /wait
RUN chmod +x /wait
CMD /wait
CMD ["python3", "/home/pyapp/py_mongo.py"]