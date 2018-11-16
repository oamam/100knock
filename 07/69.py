from flask import Flask, render_template, request
from pymongo import MongoClient
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def search():
    artist_name = request.form['name']
    aliase_name = request.form['aliase.name']
    tag = request.form['tags.value']

    conditions = {}
    if artist_name:
        conditions['name'] = artist_name
    if aliase_name:
        conditions['aliases.name'] = aliase_name
    if tag:
        conditions['tags.value'] = tag

    client = MongoClient('localhost', 27017)
    db = client.knock
    artists = db.artists
    result = artists.find(conditions)
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8989)
