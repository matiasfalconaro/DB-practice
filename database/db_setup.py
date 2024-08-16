import os
import sys
import yaml
import logging

from sqlalchemy import create_engine
from models import Base


logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)


def load_yaml(file_path: str) -> dict:
    # Hardcoded absolute path to the db_config.yaml file
    hardcoded_path = '/home/matias/Documents/DB-practice/database/db_config.yaml'
    
    # If you want to keep the flexibility of using file_path, remove the hardcoded path
    abs_path = os.path.abspath(file_path) if file_path != 'db_config.yaml' else hardcoded_path
    
    with open(abs_path, 'r') as file:
        return yaml.safe_load(file)


def get_database_url(credentials: dict, dbname: str) -> str:
    return f"postgresql+psycopg2://{credentials['user']}:{credentials['password']}@{credentials['host']}:{credentials['port']}/{dbname}"


def create_tables(engine):
    Base.metadata.create_all(engine)
    print("Tables created successfully")


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

    # Just create tables, assuming the database already exists
    create_tables(engine)
