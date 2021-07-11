# Python container app

## Project description
The python app runs as part of docker container along with other database containers  mongodb and mongo-express using docker compose.

As all the containers are in the same network created by docker compose, the app connects using the name of the mongo db service.

e.g. ***MongoClient("mongodb://admin:password@mongodb:27017")***

If the app runs as part of the host while the db runs as a container then one can use 

***MongoClient("mongodb://admin:password@<ip_addr_mongodb_container>:27017")***


To start container run:

`$ docker-compose -f mongo.yml up -d`

To stop container run:

`$ docker-compose -f mongo.yml down`