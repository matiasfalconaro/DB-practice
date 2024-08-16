#!/bin/bash
set -e  # Exit immediately if a command exits with a non-zero status

echo "Creating Python virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "Installing required Python packages..."
pip install -r requirements.txt

echo "Extracting credentials for supplychain_development..."
read DEV_USER DEV_PASSWORD < <(python3 database/extract_credentials.py supplychain_development)

echo "Extracting credentials for supplychain_production..."
read PROD_USER PROD_PASSWORD < <(python3 database/extract_credentials.py supplychain_production)

echo "Extracting credentials for supplychain_backup..."
read BACKUP_USER BACKUP_PASSWORD < <(python3 database/extract_credentials.py supplychain_backup)

echo "Pulling PostgreSQL Docker image..."
docker pull postgres

echo "Running PostgreSQL Docker container..."
docker run --name supply-chain \
  -e POSTGRES_USER=$DEV_USER \
  -e POSTGRES_PASSWORD=$DEV_PASSWORD \
  -e POSTGRES_DB=supplychain_development \
  -p 5432:5432 \
  -d postgres

echo "Waiting for PostgreSQL to initialize..."
sleep 10

echo "Creating additional PostgreSQL users and databases..."
docker exec -i supply-chain psql -U $DEV_USER -d postgres <<EOF
CREATE USER $PROD_USER WITH PASSWORD '$PROD_PASSWORD';
CREATE DATABASE supplychain_production OWNER $PROD_USER;
CREATE USER $BACKUP_USER WITH PASSWORD '$BACKUP_PASSWORD';
CREATE DATABASE supplychain_backup OWNER $BACKUP_USER;
EOF

echo "Setting up database schemas..."
databases=("supplychain_development" "supplychain_production" "supplychain_backup")
for db in "${databases[@]}"; do
    python3 database/db_setup.py "$db"
done

echo "All steps completed successfully!"
