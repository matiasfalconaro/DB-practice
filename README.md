# Supply Chain ETL

## Overview
The project is a Dockerized ETL environment featuring an API for data management, components for database schema definition, system logging, and ETL processing. It interacts with PostgreSQL databases for production, development, and backup purposes. 

## Architecture

![Project Architecture](imgs/architecture.svg)

## Data model

![Project Data model](imgs/data_model.svg)

## Run the project
```
$ chmod +x create_db_container.sh
$ ./create_db_container.sh
```