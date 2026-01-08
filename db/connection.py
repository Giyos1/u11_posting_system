import psycopg2


class DBManager:
    def __init__(self, db_name='postgres', db_user='giyos', db_password='12',
                 db_port=5432, db_host='localhost'):
        self.conn = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            port=db_port,
            host=db_host
        )

    def __enter__(self):
        return self.conn.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.commit()
            self.conn.close()

    def execute(self, query, params=None, fetch=False):
        cur = self.conn.cursor()
        cur.execute(query, params)
        result = cur.fetchall() if fetch else None
        self.conn.commit()
        cur.close()
        return result

    def close(self):
        self.conn.close()


# ---------------- DB FUNCTIONS ----------------


def get_vlogs():
    db = DBManager()
    rows = db.execute(
        "SELECT title, description, created_at FROM vlogs ORDER BY created_at DESC",
        fetch=True
    )
    db.close()
    return rows


def add_vlog(title, description):
    db = DBManager()
    db.execute(
        "INSERT INTO vlogs (title, description) VALUES (%s, %s)",
        (title, description)
    )
    db.close()
