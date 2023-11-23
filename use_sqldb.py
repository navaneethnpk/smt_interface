import sqlite3
import pandas
from sqldb import *

# data = ['434248071.0', '2023-10-06 00:27:50', '9000005870', '43373']
# data = ['438328242.0', '2023-11-22 05:50:41', '9000005940', '44073']
# data = ['438361962.0', '2023-11-22 15:12:41', '9000005940', '44078']

adddata = sqladdrow(data)

if adddata:
    print("Trigger data added to the database successfully.")
else:
    print("Failed to add Trigger data to the database.")