from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# rows = [{'no':1, 'ast':'434248071.0','utc':'2023-10-06 00:27:50','obsid':'9000005870', 'orbit':'43373', 'type':''},
#         {'no':2, 'ast':'438328242.0','utc':'2023-11-22 05:50:41','obsid':'9000005940', 'orbit':'44073', 'type':''},
#         {'no':3, 'ast':'438361962.0','utc':'2023-11-22 15:12:41','obsid':'9000005940', 'orbit':'44078', 'type':''}]

#Connect to the SQLite database
def getdatadb():
    conn = sqlite3.connect('smttriggers.db')
    cursor = conn.cursor()
    query = "SELECT * FROM triggers;"
    cursor.execute(query)
    dbrow = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    rowdata = []
    for row in dbrow:
        row_dict = dict(zip(columns, row))
        rowdata.append(row_dict)
        # print(row_dict)
    # print(rowdata)
    cursor.close()
    conn.close()
    return rowdata

@app.route("/")
def hello_czti():
    rows = getdatadb()
    return render_template('home.html', elem=rows)

if __name__ == '__main__':
    app.run(debug=True)