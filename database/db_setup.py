import os
import sys
import yaml
import logging

from sqlalchemy import create_engine, inspect
from sqlalchemy_utils import database_exists, create_database
from models import Base


logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)


def load_yaml(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)


def get_database_url(credentials: dict, dbname: str) -> str:
    return f"postgresql+psycopg2://{credentials['user']}:{credentials['password']}@{credentials['host']}:{credentials['port']}/{dbname}"


def create_tables(engine):
    Base.metadata.create_all(engine)
    print("Tables created successfully")


def get_foreign_keys(table):
    inspector = inspect(engine)
    fks = inspector.get_foreign_keys(table.__tablename__)
    return fks


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python db_setup.py <dbname>")
        sys.exit(1)

    dbname = sys.argv[1]

    # Load YAML configuration if environment variables are not set
    if not os.getenv('DB_USER'):
        config = load_yaml('db_config.yaml')
        credentials = load_yaml(config['credentials_path'])
        credentials = credentials[dbname]
    else:
        credentials = {
            'user': os.getenv('DB_USER'),
            'password': os.getenv('DB_PASSWORD'),
            'host': os.getenv('DB_HOST'),
            'port': os.getenv('DB_PORT')
        }

    db_url = get_database_url(credentials, dbname)

    engine = create_engine(db_url)

    if not database_exists(engine.url):
        print(f"Creating database {dbname}...")
        create_database(engine.url)
        print(f"Database {dbname} created successfully.")
    else:
        print(f"Database {dbname} already exists.")

    create_tables(engine)
