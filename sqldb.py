# Auther: NavaneethPK, V1.0
import sqlite3

def sqladdrow(tlist):
	status = False
	try:
		conn = sqlite3.connect('smttriggers.db')
		cursor = conn.cursor()
		trigger_info = tlist
		query = "INSERT INTO events (event_obsid, event_orbit, event_ast, event_utc) VALUES (?, ?, ?, ?);"
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
# cursor.execute("""CREATE TABLE events (event_id INTEGER PRIMARY KEY AUTOINCREMENT, event_obsid TEXT, event_orbit TEXT, event_ast TEXT, event_utc TEXT, event_type TEXT)""")

# #Adding data to sqldb 
# alldata = 'test_data.txt'
# with open(alldata, 'r') as file:
# 	lines = [line.strip() for line in file.readlines()]
# datalist = []
# for item in lines:
# 	data = item.split(',')
# 	datalist.append(data)

# for item in datalist:
# 	adddata = sqladdrow(item)
# 	print(adddata)

#Reading the table
conn = sqlite3.connect('smttriggers.db')
cursor = conn.cursor()
query = "SELECT * FROM events;"
cursor.execute(query)
rows = cursor.fetchall()
for row in rows:
	print(row)
cursor.close()
conn.close()