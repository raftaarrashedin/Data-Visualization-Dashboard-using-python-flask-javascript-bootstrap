from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://raftaarrashedin_mongodb:mUaDMb3FqKsY_Nd@cluster0.rro8gtk.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

#----------------------------------------------------------
from flask import Flask, jsonify, request
from flask_cors import CORS 
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# connect to mongodb
uri = "mongodb+srv://raftaarrashedin_mongodb:mUaDMb3FqKsY_Nd@cluster0.rro8gtk.mongodb.net/?retryWrites=true&w=majority"

# VisualizatioDashboard.Dashboard Data
client = MongoClient(uri)
db = client.get_database("VisualizatioDashboard")
collection = db["Dashboard Data"]

@app.route("/check_connection", methods=["GET"]) 
def check_connection() :
    try :
        result = collection.find_one()

        return jsonify({"message" : "Conncection to mongoDB is Successful!"})

    except Exception as e :
        return jsonify({"error":str(e)}), 500


if __name__ == "__main__" :
    app.run(debug=True)