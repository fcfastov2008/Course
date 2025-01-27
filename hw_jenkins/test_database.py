import os
import psycopg2
import pytest
import time



DB_CONFIG = {
"host": "localhost",
"port": 5432,
"database": "postgres",
"user": "postgres",
"password": "Poliklinika!"

}

def wait_for_db():
    for _ in range(50):  
        try:
            conn = psycopg2.connect(**DB_CONFIG)
            conn.close()
            return True
        except psycopg2.OperationalError:
            time.sleep(1)
    raise Exception("PostgreSQL не запустився вчасно")

wait_for_db()


@pytest.fixture
def db_connection():
    conn = psycopg2.connect(**DB_CONFIG)
    yield conn
    conn.close()

def test_connection(db_connection):
    assert db_connection is not None

def test_insert_data(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS test_table (id SERIAL PRIMARY KEY, name TEXT);")
    cursor.execute("INSERT INTO test_table (name) VALUES ('Test Name') RETURNING id;")
    db_connection.commit()
    inserted_id = cursor.fetchone()[0]
    assert inserted_id is not None

def test_select_data(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SELECT name FROM test_table WHERE name = 'Test Name';")
    result = cursor.fetchone()
    assert result is not None and result[0] == 'Test Name'

def test_delete_data(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("DELETE FROM test_table WHERE name = 'Test Name';")
    db_connection.commit()
    cursor.execute("SELECT name FROM test_table WHERE name = 'Test Name';")
    result = cursor.fetchone()
    assert result is None
