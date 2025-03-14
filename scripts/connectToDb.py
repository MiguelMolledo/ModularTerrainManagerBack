from sqlalchemy import create_engine

DATABASE_URL = "postgresql+psycopg2://postgres:yourpassword@localhost:5432/postgres"
engine = create_engine(DATABASE_URL)
print(engine.connect())  # Test connection
