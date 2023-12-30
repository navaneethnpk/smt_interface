# To print the database table
import sqlite3

DATABASE = 'smttriggers_test.db'

conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()
query = "SELECT * FROM events;"
cursor.execute(query)
rows = cursor.fetchall()
for row in rows:
        print(row)
cursor.close()
conn.close()
