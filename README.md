# Supply Chain ETL

## Overview
The project is a Dockerized ETL environment featuring an API for data management, components for database schema definition, system logging, and ETL processing. It interacts with PostgreSQL databases for production, development, and backup purposes. 

## Architecture
A Dockerized microservices architecture with FastAPI for data access, an ETL service for data processing, and PostgreSQL for storage.

![Project Architecture](imgs/architecture.svg)

## Data model
The database design is derived from an Excel (.xlsx) file

[supply_chain.xlsx](database/files/supply_chain.xlsx)

### ERD
![Project Data model](imgs/data_model.svg)

## Set up development database
```
$ python3 -m venv ven
$ source venv/bin/activate
$ pip install -r requirements.txt
$ cd database
$ docker pull postgres
$ docker run --name supply-chain -e POSTGRES_USER=development_user -e POSTGRES_PASSWORD=development_password -e POSTGRES_DB=supplychain_development -p 5432:5432 -d postgres
$ docker ps -a
$ docker exec -it supply-chain psql -U development_user -d postgres
$ python3 db_setup.py supplychain_development
```