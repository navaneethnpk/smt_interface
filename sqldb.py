# Auther: NavaneethPK, V1.0
import sqlite3

def sqladdrow(tlist):
	status = False
	try:
		conn = sqlite3.connect('smttriggers.db')
		cursor = conn.cursor()
		trigger_info = tlist
		query = "INSERT INTO triggers (ast, utc, obsid, orbit) VALUES (?, ?, ?, ?);"
		cursor.execute(query, trigger_info)
		conn.commit()
		status = True
	except sqlite3.Error as e:
		print("Error adding trigger data to the database: {}".format(e))
	finally:
		cursor.close()
		conn.close()
	return status

# # Creating the table & database
# conn = sqlite3.connect('smttriggers.db')
# cursor = conn.cursor()
# cursor.execute("""CREATE TABLE triggers (no INTEGER PRIMARY KEY AUTOINCREMENT, ast TEXT, utc TEXT, obsid TEXT, orbit TEXT, type TEXT)""")

#Reading the table
conn = sqlite3.connect('smttriggers.db')
cursor = conn.cursor()
query = "SELECT * FROM triggers;"
cursor.execute(query)
rows = cursor.fetchall()
for row in rows:
	print(row)
cursor.close()
conn.close()

#Removing a row from the database table
# row_id = 3
# conn = sqlite3.connect('smttriggers.db')
# cursor = conn.cursor()
# query = "DELETE FROM triggers WHERE no = ?;"
# cursor.execute(query, (row_id,))
# conn.commit()