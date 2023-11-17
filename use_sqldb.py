import sqlite3
import pandas
from sqldb import *

# data = ['430225512.0', '2023-08-20 11:05:12', 'CZT', '0.1', '9000005822', '42682', 'czti_430225512.0_0.1.png', 'GRB']
# data = ['430225512.0', '2023-08-20 11:05:12', 'VETO', '1.0', '9000005822', '42682', 'veto_430225512.0_1.0.png', 'GRB']
data = ['429715396.0', '2023-08-14 13:23:16', 'VETO', '1.0', '9000005818', '42682', 'veto_429715396.0_1.0.png', 'TGF']
# data = ['430039770.0', '2023-08-18 07:29:30', 'VETO', '1.0', '9000005820', '42651', 'veto_430039770.0_1.0.png', 'False']
# data = ['437886198.0', '2023-11-17 03:03:18', 'CZT', '1.0', '9000005926', '43997', 'czti_437886198.83_1.0.png', 'GRB']

adddata = sqladdrow(data)

if adddata:
    print("Trigger data added to the database successfully.")
else:
    print("Failed to add Trigger data to the database.")