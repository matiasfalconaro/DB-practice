# LOGS

## Manual execution
```
matias:~/Documents/DB-practice/ (main)$ python3 -m venv ven

matias:~/Documents/DB-practice/ (main)$ source venv/bin/activate

(venv) matias:~/Documents/DB-practice/ (main)$ pip install -r requirements.txt
Collecting greenlet==3.0.3
  Using cached greenlet-3.0.3-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (667 kB)
Processing /home/matias/.cache/pip/wheels/ad/76/94/83d0d344d36a4d846bda734160afb35b919852ca8afa53c5b9/psycopg2-2.9.9-cp38-cp38-linux_x86_64.whl
Collecting psycopg2-binary==2.9.9
  Downloading psycopg2_binary-2.9.9-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.0 MB)
     |████████████████████████████████| 3.0 MB 2.7 MB/s 
Collecting PyYAML==6.0.1
  Using cached PyYAML-6.0.1-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (736 kB)
Collecting SQLAlchemy==2.0.32
  Downloading SQLAlchemy-2.0.32-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.1 MB)
     |████████████████████████████████| 3.1 MB 4.1 MB/s 
Collecting SQLAlchemy-Utils==0.41.2
  Downloading SQLAlchemy_Utils-0.41.2-py3-none-any.whl (93 kB)
     |████████████████████████████████| 93 kB 1.3 MB/s 
Collecting typing_extensions==4.12.2
  Using cached typing_extensions-4.12.2-py3-none-any.whl (37 kB)
Installing collected packages: greenlet, psycopg2, psycopg2-binary, PyYAML, typing-extensions, SQLAlchemy, SQLAlchemy-Utils
Successfully installed PyYAML-6.0.1 SQLAlchemy-2.0.32 SQLAlchemy-Utils-0.41.2 greenlet-3.0.3 psycopg2-2.9.9 psycopg2-binary-2.9.9 typing-extensions-4.12.2

(venv) matias:~/Documents/DB-practice/ (main)$ cd database

(venv) matias:~/Documents/DB-practice/database (main)$ docker pull postgres
Using default tag: latest
latest: Pulling from library/postgres
Digest: sha256:c62fdb7fd6f519ef425c54760894c74e8d0cb04fbf4f7d3d79aafd86bae24edd
Status: Image is up to date for postgres:latest
docker.io/library/postgres:latest

(venv) matias:~/Documents/DB-practice/database (main)$ docker run --name supply-chain -e POSTGRES_USER=<DEVELOPMENT_USER> -e POSTGRES_PASSWORD=<DEVELOPMENT_PASSWORD> -e POSTGRES_DB=supplychain_development -p 5432:5432 -d postgres
dbf093bf0c5eeb7cec506be09e82fb481101b4a464b2e0401eb1cfb923272944

(venv) matias:~/Documents/DB-practice/database (main)$ docker ps -a
CONTAINER ID   IMAGE      COMMAND                  CREATED          STATUS          PORTS                                       NAMES
dbf093bf0c5e   postgres   "docker-entrypoint.s…"   16 minutes ago   Up 16 minutes   0.0.0.0:5432->5432/tcp, :::5432->5432/tcp   supply-chain

(venv) matias:~/Documents/DB-practice/database (main)$ docker exec -it supply-chain psql -U <DEVELOPMENT_USER> -d postgres
psql (16.4 (Debian 16.4-1.pgdg120+1))
Type "help" for help.

postgres=# \l
                                                          List of databases
          Name           |         Owner        | Encoding | Locale Provider |  Collate   |   Ctype    | ICU Locale | ICU Rules | Access privileges 
-------------------------+----------------------+----------+-----------------+------------+------------+------------+-----------+-------------------
 postgres                | <DEVELOPMENT_USER>   | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | 
 supplychain_development | <DEVELOPMENT_USER>   | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | 
 template0               | <DEVELOPMENT_USER>   | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | =c/<DEVELOPMENT_USER>        +
                         |                      |          |                 |            |            |            |           | <DEVELOPMENT_USER>=CTc/<DEVELOPMENT_USER>
 template1               | <DEVELOPMENT_USER>   | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | =c/<DEVELOPMENT_USER>        +
                         |                      |          |                 |            |            |            |           | <DEVELOPMENT_USER>=CTc/<DEVELOPMENT_USER>
(4 rows)

postgres=# CREATE USER <PRODUCTION_USER> WITH PASSWORD '<PRODUCTION_PASSWORD>';
CREATE ROLE

postgres=# CREATE DATABASE supplychain_production OWNER <PRODUCTION_USER>;
CREATE DATABASE

postgres=# CREATE USER <BACKUP_USER> WITH PASSWORD '<BACKUP_PASSWORD>';
CREATE ROLE

postgres=# CREATE DATABASE supplychain_backup OWNER <BACKUP_USER>;
CREATE DATABASE

postgres=# \l
                                                            List of databases
          Name           |          Owner         | Encoding | Locale Provider |  Collate   |   Ctype    | ICU Locale | ICU Rules | Access privileges 
-------------------------+------------------------+----------+-----------------+------------+------------+------------+-----------+-------------------
 postgres                | <DEVELOPMENT_USER>     | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | 
 supplychain_backup      | <BACKUP_USER>          | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | 
 supplychain_development | <DEVELOPMENT_USER>     | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | 
 supplychain_production  | <PRODUCTION_USER>      | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | 
 template0               | <DEVELOPMENT_USER>     | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | =c/<DEVELOPMENT_USER>        +
                         |                        |          |                 |            |            |            |           | <DEVELOPMENT_USER>=CTc/<DEVELOPMENT_USER>
 template1               | <DEVELOPMENT_USER>     | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | =c/<DEVELOPMENT_USER>        +
                         |                        |          |                 |            |            |            |           | <DEVELOPMENT_USER>=CTc/<DEVELOPMENT_USER>
(6 rows)

postgres=# \c supplychain_development
You are now connected to database "supplychain_development" as user "<DEVELOPMENT_USER>".

supplychain_development=# \dt
Did not find any relations.

supplychain_development=# \q

(venv) matias:~/Documents/DB-practice/database (main)$ python3 db_setup.py supplychain_development
Tables created successfully

(venv) matias:~/Documents/DB-practice/database (main)$ python3 db_setup.py supplychain_production
Tables created successfully

(venv) matias:~/Documents/DB-practice/database (main)$ python3 db_setup.py supplychain_backup
Tables created successfully

(venv) matias:~/Documents/DB-practice/database (main)$ docker exec -it supply-chain psql -U <DEVELOPMENT_USER> -d postgres
psql (16.4 (Debian 16.4-1.pgdg120+1))
Type "help" for help.

postgres=# \c supplychain_development
You are now connected to database "supplychain_development" as user "<DEVELOPMENT_USER>".

supplychain_development=# \dt
            List of relations
 Schema |     Name      | Type  |      Owner      
--------+---------------+-------+-----------------
 public | categories    | table | <DEVELOPMENT_USER>
 public | customers     | table | <DEVELOPMENT_USER>
 public | employees     | table | <DEVELOPMENT_USER>
 public | logs          | table | <DEVELOPMENT_USER>
 public | order_details | table | <DEVELOPMENT_USER>
 public | orders        | table | <DEVELOPMENT_USER>
 public | products      | table | <DEVELOPMENT_USER>
 public | shippers      | table | <DEVELOPMENT_USER>
 public | suppliers     | table | <DEVELOPMENT_USER>
 public | users         | table | <DEVELOPMENT_USER>
(10 rows)

supplychain_development=# \d orders
                                            Table "public.orders"
   Column    |            Type             | Collation | Nullable |                 Default                  
-------------+-----------------------------+-----------+----------+------------------------------------------
 order_id    | integer                     |           | not null | nextval('orders_order_id_seq'::regclass)
 customer_id | integer                     |           | not null | 
 shipper_id  | integer                     |           | not null | 
 employee_id | integer                     |           | not null | 
 order_date  | timestamp without time zone |           |          | 
Indexes:
    "orders_pkey" PRIMARY KEY, btree (order_id)
Foreign-key constraints:
    "orders_customer_id_fkey" FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
    "orders_employee_id_fkey" FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
    "orders_shipper_id_fkey" FOREIGN KEY (shipper_id) REFERENCES shippers(shipper_id)
Referenced by:
    TABLE "order_details" CONSTRAINT "order_details_order_id_fkey" FOREIGN KEY (order_id) REFERENCES orders(order_id)

postgres=# \q
(venv) matias:~/Documents/DB-practice/database (main)$ 
```

## Automated execution
```
matias:~/Documents/DB-practice (main)$ ./main.sh
Creating Python virtual environment...
Installing required Python packages...
Requirement already satisfied: greenlet==3.0.3 in ./venv/lib/python3.8/site-packages (from -r requirements.txt (line 1)) (3.0.3)
Requirement already satisfied: psycopg2==2.9.9 in ./venv/lib/python3.8/site-packages (from -r requirements.txt (line 2)) (2.9.9)
Requirement already satisfied: psycopg2-binary==2.9.9 in ./venv/lib/python3.8/site-packages (from -r requirements.txt (line 3)) (2.9.9)
Requirement already satisfied: PyYAML==6.0.1 in ./venv/lib/python3.8/site-packages (from -r requirements.txt (line 4)) (6.0.1)
Requirement already satisfied: SQLAlchemy==2.0.32 in ./venv/lib/python3.8/site-packages (from -r requirements.txt (line 5)) (2.0.32)
Requirement already satisfied: SQLAlchemy-Utils==0.41.2 in ./venv/lib/python3.8/site-packages (from -r requirements.txt (line 6)) (0.41.2)
Requirement already satisfied: typing_extensions==4.12.2 in ./venv/lib/python3.8/site-packages (from -r requirements.txt (line 7)) (4.12.2)
Extracting credentials for supplychain_development...
Extracting credentials for supplychain_production...
Extracting credentials for supplychain_backup...
Pulling PostgreSQL Docker image...
Using default tag: latest
latest: Pulling from library/postgres
Digest: sha256:c62fdb7fd6f519ef425c54760894c74e8d0cb04fbf4f7d3d79aafd86bae24edd
Status: Image is up to date for postgres:latest
docker.io/library/postgres:latest
Running PostgreSQL Docker container...
c9495ced6bbe8397843a4853b3adc9ae5d3d84af4b5a223da8ddd90d6ab84270
Waiting for PostgreSQL to initialize...
Creating additional PostgreSQL users and databases...
CREATE ROLE
CREATE DATABASE
CREATE ROLE
CREATE DATABASE
Setting up database schemas...
Tables created successfully
Tables created successfully
Tables created successfully
All steps completed successfully!

matias:~/Documents/DB-practice (main)$ docker ps -a
CONTAINER ID   IMAGE      COMMAND                  CREATED          STATUS          PORTS                                       NAMES
c9495ced6bbe   postgres   "docker-entrypoint.s…"   19 seconds ago   Up 19 seconds   0.0.0.0:5432->5432/tcp, :::5432->5432/tcp   supply-chain

matias:~/Documents/DB-practice (main)$ docker exec -it supply-chain psql -U <DEVELOPMENT_USER> -d postgres
psql (16.4 (Debian 16.4-1.pgdg120+1))
Type "help" for help.

postgres=# \l
                                                            List of databases
          Name           |         Owner       | Encoding | Locale Provider |  Collate   |   Ctype    | ICU Locale | ICU Rules | Access privileges 
-------------------------+---------------------+----------+-----------------+------------+------------+------------+-----------+-------------------
 postgres                | <DEVELOPMENT_USER>  | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | 
 supplychain_backup      | <BACKUP_USER>       | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | 
 supplychain_development | <DEVELOPMENT_USER>  | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | 
 supplychain_production  | <PRODUCTION_USER>   | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | 
 template0               | <DEVELOPMENT_USER>  | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | =c/<DEVELOPMENT_USER>        +
                         |                     |          |                 |            |            |            |           | <DEVELOPMENT_USER>=CTc/<DEVELOPMENT_USER>
 template1               | <DEVELOPMENT_USER>  | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | =c/<DEVELOPMENT_USER>        +
                         |                     |          |                 |            |            |            |           | <DEVELOPMENT_USER>=CTc/<DEVELOPMENT_USER>
(6 rows)

postgres=# \c supplychain_development
You are now connected to database "supplychain_development" as user "<DEVELOPMENT_USER>".

supplychain_development=# \dt
            List of relations
 Schema |     Name      | Type  |       Owner       
--------+---------------+-------+-------------------
 public | categories    | table | <DEVELOPMENT_USER>
 public | customers     | table | <DEVELOPMENT_USER>
 public | employees     | table | <DEVELOPMENT_USER>
 public | logs          | table | <DEVELOPMENT_USER>
 public | order_details | table | <DEVELOPMENT_USER>
 public | orders        | table | <DEVELOPMENT_USER>
 public | products      | table | <DEVELOPMENT_USER>
 public | shippers      | table | <DEVELOPMENT_USER>
 public | suppliers     | table | <DEVELOPMENT_USER>
 public | users         | table | <DEVELOPMENT_USER>
(10 rows)

supplychain_development=# \d orders
                                            Table "public.orders"
   Column    |            Type             | Collation | Nullable |                 Default                  
-------------+-----------------------------+-----------+----------+------------------------------------------
 order_id    | integer                     |           | not null | nextval('orders_order_id_seq'::regclass)
 customer_id | integer                     |           | not null | 
 shipper_id  | integer                     |           | not null | 
 employee_id | integer                     |           | not null | 
 order_date  | timestamp without time zone |           |          | 
Indexes:
    "orders_pkey" PRIMARY KEY, btree (order_id)
Foreign-key constraints:
    "orders_customer_id_fkey" FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
    "orders_employee_id_fkey" FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
    "orders_shipper_id_fkey" FOREIGN KEY (shipper_id) REFERENCES shippers(shipper_id)
Referenced by:
    TABLE "order_details" CONSTRAINT "order_details_order_id_fkey" FOREIGN KEY (order_id) REFERENCES orders(order_id)

supplychain_development=# \q
```