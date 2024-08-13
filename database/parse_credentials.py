import yaml

def load_credentials(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

if __name__ == "__main__":
    credentials = load_credentials('database/credentials.yaml')
    for section, creds in credentials.items():
        section = section.lower().replace(' ', '_')
        print(f"export {section}_user={creds['user']}")
        print(f"export {section}_password={creds['password']}")
        print(f"export {section}_host={creds['host']}")
        print(f"export {section}_port={creds['port']}")
