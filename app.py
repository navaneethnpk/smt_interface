from flask import Flask, render_template

app = Flask(__name__)

rows = [{'id':1, 'ast':'430225512.0', 'utc':'2023-08-20 11:05:12', 'detector':'CZT', 'binning':'0.1', 'obsid':'9000005822', 'orbit':'42682', 'plot':'static/czti_430225512.0_0.1.png', 'type':'GRB'}, {'id':2, 'ast':'430225512.0', 'utc':'2023-08-20 11:05:12', 'detector':'VETO', 'binning':'1.0', 'obsid':'9000005822', 'orbit':'42682', 'plot':'static/veto_430225512.0_1.0.png', 'type':'GRB'}, {'id':3, 'ast':'429715396.0', 'utc':'2023-08-14 13:23:16', 'detector':'VETO', 'binning':'1.0', 'obsid':'9000005818', 'orbit':'42682', 'plot':'static/veto_429715396.0_1.0.png', 'type':'TGF'}]

@app.route("/")
def hello_czti():
    return render_template('home.html', elem=rows)

if __name__ == '__main__':
    app.run(debug=True)