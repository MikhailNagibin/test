import json
import psycopg2
import requests

def get_db_connection() -> psycopg2.extensions.connection:
    with open("config.json") as f:
        conf = json.load(f)
    DATABASE = conf["DATABASE"]
    USER = conf["USER"]
    PASSWORD = conf["PASSWORD"]
    HOST = conf["HOST"]
    PORT = conf["PORT"]
    conn = psycopg2.connect(
        dbname=DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT
    )
    return conn


def get_all_days() -> dict:
    return requests.get('http://127.0.0.1:5000/date').json()


def information_by_day(date: str) -> dict:
    day, month, year = date.split('-')
    return requests.get('http://127.0.0.1:5000', {'day': day,'month': month, 'year': year}).json()


def get_date_id(cur: psycopg2.extensions.cursor, date: int) -> int:
    cur.execute("select id from dates where date = ?", (date, ))
    ans = cur.fetchall()
    if ans:
        return ans[0]
    return -1


def insert_days_in_db(conn: psycopg2.extensions.connection, data: dict):
    cur = conn.cursor()
    print(data['date']['data'])
    cur.execute("insert into dates(date) values %s", (data['date']['data'], ))
