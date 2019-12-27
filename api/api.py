import os
import json

from flask import Flask
from flask_restplus import Resource, Api
from flask_restplus import reqparse

import pymongo
from bson import json_util


# TODO (James): what's best practice for hosting the client?
# How do I always open a new client on each request?

MONGODB_LOCATION = os.environ.get("MONGODB_LOCATION", "mongodb://localhost:27017/")
DB_CLIENT = pymongo.MongoClient(MONGODB_LOCATION)
DB_DATABASE = DB_CLIENT["metadata"]  # metadata is the db name.

# Flask app start.
app = Flask(__name__)
api = Api(app)

# Get arguments for /dog endpoint.
dog_metadata_request_parser = reqparse.RequestParser()
dog_metadata_request_parser.add_argument(
    "dog_type", type=str, help="Type of dog, full folder name."
)


@api.route("/dog")
@api.expect(dog_metadata_request_parser)
class Dog(Resource):
    def post(self):
        args = dog_metadata_request_parser.parse_args()
        dog_type = args["dog_type"]

        # ObjectId needs to be parsed, then we return it to json for the user.
        return json.loads(json_util.dumps(DB_DATABASE["dogs"].find({"Name": dog_type})))


# List all users for some reason
@api.route("/users")
class User(Resource):
    def get(self):
        return DB_DATABASE["users"].find()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
