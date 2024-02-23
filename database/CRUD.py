import sqlite3

"""try pandas"""


class DataBaseCRUD:
    """
    management panel for database using sqllite3 module
    """

    def __init__(self, db_path: str):
        """initializing connection for db"""
        conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn = conn
        self.cursor = conn.cursor()


if __name__ == '__main__':
    table = DataBaseCRUD('test_database.db')
