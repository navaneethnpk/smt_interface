from flask import Flask, render_template, request, redirect, url_for, g, session
import sqlite3

app = Flask(__name__)
DATABASE = 'smttriggers.db'

#Connect to the SQLite database
def getdatadb():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    query = "SELECT * FROM events;"
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

# Update event type in the database
def update_event_type(event_id, event_type):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    query = "UPDATE events SET event_type = ? WHERE event_id = ?;"
    cursor.execute(query, (event_type, event_id))
    conn.commit()
    cursor.close()
    conn.close()

@app.route("/", methods=['GET', 'POST'])
def hello_czti():
    if request.method == 'POST':
        event_id = request.form['event_id']
        event_type = request.form['event_type']
        update_event_type(event_id, event_type)
    
    rows = getdatadb()
    return render_template('index.html', elem=rows)

@app.route("/grb")
def grb_page():
    rows = getdatadb()
    return render_template('grb.html', elem=rows)

@app.route("/tgf")
def tgf_page():
    rows = getdatadb()
    return render_template('tgf.html', elem=rows)

@app.route("/solar")
def solar_page():
    rows = getdatadb()
    return render_template('solar.html', elem=rows)

@app.route("/false")
def false_page():
    rows = getdatadb()
    return render_template('false.html', elem=rows)

if __name__ == '__main__':
    app.run(debug=True)
