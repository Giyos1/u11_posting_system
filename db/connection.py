import psycopg2


import psycopg2

class DBManager:
    def __init__(self, db_name='postgres', db_user='postgres', db_password='atash',
                 db_port=5432, db_host='localhost'):
        self.conn = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            port=db_port,
            host=db_host
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.conn.rollback()
        else:
            self.conn.commit()
        self.conn.close()

    def execute(self, query, params=None, fetch=False):
        with self.conn.cursor() as cur:
            cur.execute(query, params)
            if fetch:
                return cur.fetchall()



# ---------------- DB FUNCTIONS ----------------


def get_vlogs():
    with DBManager() as db:
        return db.execute(
            "SELECT id, title, description, created_at FROM vlogs ORDER BY created_at DESC",
            fetch=True
        )

def add_vlog(title, description):
    with DBManager() as db:
        db.execute(
            "INSERT INTO vlogs (title, description) VALUES (%s, %s)",
            (title, description)
        )

def delete_vlog(id):
    with DBManager() as db:
        db.execute(
            "DELETE FROM vlogs WHERE id = %s",
            (id,)
        )


