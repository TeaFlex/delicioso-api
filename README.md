# Delicioso-api
REST API project to practice the django framwork.

## Installation
```
pipenv install
```

## Database
To make the database configuration easier, create a docker container as such:
```
docker create -p 5432:5432 --name postgredev -e POSTGRES_PASSWORD=goodpassword -e POSTGRES_USER=postdev -e POSTGRES_DB=delicioso_db postgres
```

Or you can edit the dev.env file to configure the app to use your own PostgreSQL server.
