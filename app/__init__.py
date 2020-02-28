from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS
app = Flask(__name__)

CONNECTION_STRING = "mongodb+srv://jopotochny:agiraffeisalonghorse@cluster0-egpxu.mongodb.net/test?authSource=admin&replicaSet=Cluster0-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true"
app.config["MONGO_URI"] = CONNECTION_STRING

mongo = PyMongo(app)
cors = CORS(app)
client = mongo.cx
db = client['MonsterHunterHelperDB']

from app import routes
