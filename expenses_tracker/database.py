import sqlite3
from sqlite3 import Error
from sqlite3 import Connection

def make_connection(filename):
    # Creates or connects to the expenses database
    conn = None
    try:
        conn = sqlite3.connect(filename)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn

def create_table(conn, table_params):
    # Creates table within the specified database if none exists with the given parameters
    try:
        c = conn.cursor()
        c.execute(table_params)
    except Error as e:
        print(e)

def connect_expense_db(conn):
    # Creates expenses database if none exists
    expenses_db = '''CREATE TABLE IF NOT EXISTS expenses (
        id integer PRIMARY KEY,
        currency text NOT NULL,
        amount float NOT NULL,
        date text NOT NULL
    ); '''
    if conn is not None:
        create_table(conn, expenses_db)
    else:
        print('Error! Could not connect to database.')

def insert_expense(conn, expense):
    # Adds the defined expense into the expenses database
    expense_data = (expense.currency, expense.amount, str(expense.date))
    sql = '''INSERT INTO expenses(currency,amount,date) VALUES(?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, expense_data)
    print(sqlite3.version)
    conn.commit()
    return cur.lastrowid

def delete_all(conn):
    sql = '''DELETE * FROM expenses'''
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    print('Expenses deleted')

def fetch_all(conn):
    sql = '''SELECT * FROM expenses'''
    cur = conn.cursor()
    cur.execute(sql)
    expenses = cur.fetchall()
    return(expenses)
