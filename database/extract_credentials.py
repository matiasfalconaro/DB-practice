import yaml
import sys


def load_credentials(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)


if __name__ == "__main__":
    credentials = load_credentials('database/credentials.yaml')
    
    section = sys.argv[1]
    
    user = credentials[section]['user']
    password = credentials[section]['password']
