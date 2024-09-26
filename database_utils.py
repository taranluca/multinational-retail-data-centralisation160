import yaml
from sqlalchemy import create_engine 
from sqlalchemy import inspect
class DatabaseConnector:
    def __init__(self,filename):
        self.filename = filename

    def read_db_creds(self):
        with open(self.filename,"r") as file:
            cred_file = yaml.safe_load(file)
        return cred_file

    def init_db_engine(self):
        creds = self.read_db_creds()
        engine = create_engine(f"{"postgresql"}+{"psycopg2"}://{creds["RDS_USER"]}:{creds["RDS_PASSWORD"]}@{creds["RDS_HOST"]}:{creds["RDS_PORT"]}/{creds["RDS_DATABASE"]}")
        return engine

    def list_db_tables(self,engine):
        inspector = inspect(engine)
        result = inspector.get_table_names()
        return result
    
db_connector = DatabaseConnector("db_creds.yaml")
engine = db_connector.init_db_engine()
tables = db_connector.list_db_tables(engine)