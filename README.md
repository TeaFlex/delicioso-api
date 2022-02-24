# Delicioso-api
REST API project to practice the django framwork.

## Installation
```
pipenv install
```

## Docker image

You can build a Docker image from the Dockerfile by followinf these steps:
- Copy the `dev.env` file to `.env`:
    ```
    cp ./dev.env ./.env
    ```
- Change the values inside the `.env` file to match your needs.
- Change the exposed port in the Docker file (default: 8000).
- Build your image:
    ```
    docker build -t delicioso .
    ```

## Database
To make the database configuration easier, create a docker container as such:
```
docker create -p 5432:5432 --name postgredev -e POSTGRES_PASSWORD=goodpassword -e POSTGRES_USER=postdev -e POSTGRES_DB=delicioso_db postgres
```

Or you can edit the dev.env file to configure the app to use your own PostgreSQL server.
