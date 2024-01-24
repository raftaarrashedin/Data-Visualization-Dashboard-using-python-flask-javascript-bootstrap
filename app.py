#-----------------------------------------------------
#-----------------------------------------------------
#-----------------------------------------------------
from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient

#-----------------------------------------------------
#-----------------------------------------------------
#-----------------------------------------------------
app = Flask(__name__)
CORS(app)

#-----------------------------------------------------
#-----------------------------------------------------
#-----------------------------------------------------
# Connect to MongoDB
uri = "mongodb+srv://raftaarrashedin_mongodb:mUaDMb3FqKsY_Nd@cluster0.rro8gtk.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client.get_database("mongoDB_pkg")
collection = db["dashboard_data"]

#-----------------------------------------------------
#-----------------------------------------------------
#-----------------------------------------------------
# Define a simple root endpoint
@app.route("/", methods=["GET"])
def index():
    filters = request.args.to_dict()

    # convert string values to appropriate types if needed
    for key, value in filters.items():
        if value.isdigit():
            filters[key] = int(value)

    filtered_data = collection.find(filters, {"id": 0})
    result = list(filtered_data)

    # Convert ObjectId to string representation
    for item in result:
        item["_id"] = str(item["_id"])

    return jsonify({"data": result})

#-----------------------------------------------------
#-----------------------------------------------------
#-----------------------------------------------------
# Check connection endpoint
@app.route("/check_connection", methods=["GET"])
def check_connection():
    try:
        # Check if you can perform a simple operation on the collection
        result = collection.find_one()
        return jsonify({"message": "Connection to MongoDB is successful!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#-----------------------------------------------------
#-----------------------------------------------------
#-----------------------------------------------------
# running app
if __name__ == "__main__":
    app.run(debug=True)
