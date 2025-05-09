import sqlite3
from contextlib import closing

db_path = "sqlite3 (1).db"

try:
    with closing(sqlite3.connect(db_path)) as db_con:
        db_con.row_factory = sqlite3.Row
        with closing(db_con.cursor()) as cursor:
            try:
                query_1 = "SELECT * FROM demo WHILE id > 14"
                cursor.execute(query_1)
                rows = cursor.fetchall()
                print("Name of rows with id >14: ")
                for row in rows:
                    print(row["name"])
            except Exception as e:
                print(f"Error executing query_1: {e}")

            try:
                del_row = input("Enter the row ID threshold for deletion: ")
                query_2 = "DELETE FROM demo WHERE id < ?"
                cursor.execute(query_2, (del_row,))
                num_rows = cursor.rowcount
                print(f"{num_rows} rows affected. Are you sure you want to continue?")
                db_con.commit()
            except Exception as e:
                print(f"Error executing query_2: {e}")

except ValueError:
    print("---")