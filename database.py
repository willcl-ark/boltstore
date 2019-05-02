import sqlite3

sqlite_file = 'my_first_db.sqlite'    # name of the sqlite database file
table_name1 = 'my_table_1'  # name of the table to be created
table_name2 = 'my_table_2'  # name of the table to be created
new_field = 'my_1st_column' # name of the column
field_type = 'INTEGER'  # column data type


# data types #
# INTEGER: A signed integer up to 8 bytes depending on the magnitude of the value.
# REAL: An 8-byte floating point value.
# TEXT: A text string, typically UTF-8 encoded (depending on the database encoding).
# BLOB: A blob of data (binary large object) for storing binary data.
# NULL: A NULL value, represents missing data or an empty cell.
##############


def connect(database):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    return conn, cursor


def commit_and_close(conn):
    conn.commit()
    conn.close()


def create_table(database, table_name, column_name, column_type):
    """
    Create table with a primary column
    """
    conn, cursor = connect(database)
    cursor.execute(f'CREATE TABLE {table_name} ({column_name} {column_type} PRIMARY KEY)')
    commit_and_close(conn)


def add_column(database, table_name, column_name, column_type):
    conn, cursor = connect(database)
    cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN '{column_name}' {column_type}")
    commit_and_close(conn)


def insert_row(database, table_name, *args):
    conn, cursor = connect(database)
    # if you add more columns, add more question marks after VALUES
    cursor.execute(f"INSERT OR IGNORE INTO {table_name} VALUES (?, ?)", tuple(args))
    commit_and_close(conn)
