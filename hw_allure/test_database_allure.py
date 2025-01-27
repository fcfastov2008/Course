import os
import psycopg2
import pytest
import time
import allure

time.sleep(20)

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD")
}

@pytest.fixture
def db_connection():
    with allure.step("Establishing database connection"):
        conn = psycopg2.connect(**DB_CONFIG)
    yield conn
    with allure.step("Closing database connection"):
        conn.close()

@allure.feature("Database Connection")
def test_connection(db_connection):
    with allure.step("Checking if connection is established"):
        assert db_connection is not None

@allure.feature("Database Operations")
def test_insert_data(db_connection):
    with allure.step("Inserting data into the table"):
        cursor = db_connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS test_table (id SERIAL PRIMARY KEY, name TEXT);")
        cursor.execute("INSERT INTO test_table (name) VALUES ('Test Name') RETURNING id;")
        db_connection.commit()
        inserted_id = cursor.fetchone()[0]
    with allure.step("Verifying that the data was inserted"):
        assert inserted_id is not None

@allure.feature("Database Operations")
def test_select_data(db_connection):
    with allure.step("Selecting data from the table"):
        cursor = db_connection.cursor()
        cursor.execute("SELECT name FROM test_table WHERE name = 'Test Name';")
        result = cursor.fetchone()
    with allure.step("Verifying selected data"):
        assert result is not None and result[0] == 'Test Name'

@allure.feature("Database Operations")
def test_delete_data(db_connection):
    with allure.step("Deleting data from the table"):
        cursor = db_connection.cursor()
        cursor.execute("DELETE FROM test_table WHERE name = 'Test Name';")
        db_connection.commit()
    with allure.step("Verifying that the data was deleted"):
        cursor.execute("SELECT name FROM test_table WHERE name = 'Test Name';")
        result = cursor.fetchone()
        assert result is None
