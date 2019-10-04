# Scheme: "postgres+psycopg2://<USERNAME>:<PASSWORD>@<IP_ADDRESS>:<PORT>/<DATABASE_NAME>"
import json

with open('config.json', 'r') as infile:
    data = json.load(infile)


DATABASE_URI = 'postgres+psycopg2://postgres:{}@localhost:{}/{}'.format(data['password'], data['port'], data['server_name'])