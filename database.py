import sqlite3

from utilities import sha256_of_hex_to_hex


# data types #
# INTEGER: A signed integer up to 8 bytes depending on the magnitude of the value.
# REAL: An 8-byte floating point value.
# TEXT: A text string, typically UTF-8 encoded (depending on the database encoding).
# BLOB: A blob of data (binary large object) for storing binary data.
# NULL: A NULL value, represents missing data or an empty cell.
##############


class Database:

    def __init__(self, sqlite_file):
        self.db = sqlite_file
        self.conn = sqlite3.connect(self.db)
        self.cursor = self.conn.cursor()
        # helper function to create sha256 hash of hex item. returns hex
        self.conn.create_function("sha256_hex_hex", 1, sha256_of_hex_to_hex)

    def reconnect(self):
        try:
            self.conn.close()
        except sqlite3.Error:
            pass
        self.conn = sqlite3.connect(self.db)
        self.cursor = self.conn.cursor()

    def close_connection(self):
        self.conn.close()

    def create_table(self, table_name, column_name, column_type):
        """
        Create table with a primary column
        """
        self.cursor.execute(f'CREATE TABLE {table_name} ({column_name} {column_type} PRIMARY KEY)')
        self.conn.commit()

    def add_column(self, table_name, column_name, column_type):
        self.cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN '{column_name}' {column_type}")
        self.conn.commit()

    def insert_row(self, table_name, *args):
        # if you add more columns, add more question marks after VALUES
        self.conn.execute(f"INSERT OR IGNORE INTO {table_name} VALUES (?, ?, ?, ?)", tuple(args))
        self.conn.commit()
