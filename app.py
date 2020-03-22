#!/usr/bin/python3

#imports

from pymongo import MongoClient
from flask import Flask
from flask_pymongo import PyMongo 
from flask import render_template


# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient('mongodb://127.0.01:27017')

db=client.test

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017"
mongo = PyMongo(app)

#Controllers

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/assets')
def assets():
    #assetdb = list(assets.find())
    assetdb = db.assets.find()
    return render_template("assets.html", asset_info=assetdb)

#Error Handlers



#Launch

if __name__ == '__main__':
    app.run(host='0.0.0.0')