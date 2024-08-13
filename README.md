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

## Run the project
```
$ source venv/bin/activate
$ pip install -r requirements.txt
$ chmod +x create_db_container.sh
$ ./create_db_container.sh
```