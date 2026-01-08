import os
from db.connection import DBManager

MIGRATIONS_DIR = "db/migrations"


def ensure_migrations_table(conn):
    conn.execute("""
                 CREATE TABLE IF NOT EXISTS migrations
                 (
                     id       SERIAL PRIMARY KEY,
                     filename TEXT UNIQUE
                 );
                 """)


def get_applied_migrations(conn):
    conn.execute("SELECT filename FROM migrations")
    return {row[0] for row in conn.fetchall()}


def apply_migration(conn, filename):
    path = os.path.join(MIGRATIONS_DIR, filename)

    with open(path, "r") as f:
        sql = f.read()

    conn.execute(sql)
    conn.execute(
        "INSERT INTO migrations (filename) VALUES (%s)",
        (filename,)
    )

    print(f"✅ Applied: {filename}")


def migrate():
    with DBManager() as curr:
        ensure_migrations_table(curr)

    with DBManager() as curr:
        applied = get_applied_migrations(curr)

    files = sorted(os.listdir(MIGRATIONS_DIR))

    for file in files:
        if file.endswith(".sql") and file not in applied:
            with DBManager() as curr:
                apply_migration(curr, file)

    print("🎉 All migrations applied!")


if __name__ == "__main__":
    migrate()
