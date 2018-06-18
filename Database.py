import sqlite3
from datetime import datetime






def create_connection():
    connection = sqlite3.connect('database.sqlite')
    return connection


def close_connection(connection):
    connection.commit()
    connection.close()
    return True


def create_Table():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        'CREATE TABLE "job" ("name" VARCHAR, "status" VARCHAR, "time" DATETIME)'
    )
    close_connection(connection)


def add_job_status(job_data):
    name, status = job_data
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        'INSERT INTO "jobs" (name, status, time) VALUES (?, ?, ?)',
        (name, status, datetime.now())
    )
    close_connection(connection)
