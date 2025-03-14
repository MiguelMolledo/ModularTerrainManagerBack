# ModularTerrainManagerBack
FastApi rest that would provide support for ModularTerrainManager App ## Create a new venv

## Install requirements
```shell
## Create a new venv
python3  -m venv "name of the venv"

# Dependencies
pip install fastapi
pip install uvicorn

```
#  Launch uvicorn server 

```shell

uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

# Postgress DB

Install in wsl 

```shell
sudo apt install postgresql postgresql-contrib -y
sudo service postgresql start
sudo service postgresql status
sudo -i -u postgres
psql
postgres=#
ALTER USER postgres PASSWORD 'yourpassword';
\q
sudo systemctl enable postgresql
# External connections 
sudo nano /etc/postgresql/14/main/postgresql.conf
# find
# listen_addresses = 'localhost'
#change it to 
listen_addresses = '*'
# open pg_hba.conf
sudo nano /etc/postgresql/14/main/pg_hba.conf
# Add this line at the bottom to allow all connections:
host all all 0.0.0.0/0 md5

# restart postgresql
sudo service postgresql restart
sudo service postgresql status

# create bew /database 
sudo -i -u postgres
psql
CREATE DATABASE mydatabase;
CREATE USER myuser WITH ENCRYPTED PASSWORD 'mypassword';
GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;
\q
exit

```

