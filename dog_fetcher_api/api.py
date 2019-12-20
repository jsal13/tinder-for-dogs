from flask import Flask
from flask_restplus import Resource, Api
from flask_restplus import reqparse


app = Flask(__name__)
api = Api(app)

# Get arguments for /fetch-dog endpoint.
dog_request_parser = reqparse.RequestParser()
dog_request_parser.add_argument(
    "dog_type", type=str, help="Type of dog, full folder name."
)


@api.route("/fetch-dog")
@api.expect(dog_request_parser)
class FetchDog(Resource):
    def post(self):
        args = dog_request_parser.parse_args()
        dog_type = args["dog_type"]

        return {"dog_type": dog_type}


# Get arguments for /fetch-user-preference endpoint.
user_preference_request_parser = reqparse.RequestParser()
user_preference_request_parser.add_argument(
    "dog_type", type=str, help="Type of dog, full folder name."
)


@api.route("/fetch-user-preference")
@api.expect(user_preference_request_parser)
class FetchUserPreference(Resource):
    def get(self):
        args = dog_request_parser.parse_args()
        dog_type = args["dog_type"]

        return {"dog_type": dog_type}


if __name__ == "__main__":
    app.run(debug=True)
