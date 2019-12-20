from flask import Flask
from flask_restplus import Resource, Api, reqparse


app = Flask(__name__)
api = Api(app)

# Get arguments for /dog endpoint.
dog_reqparse = reqparse.RequestParser()
dog_reqparse.add_argument("dog_type", type=str, help="Type of dog, full folder name.")


@api.route("/dog")
@api.expect(dog_reqparse)
class FetchDog(Resource):
    def get(self):
        args = dog_reqparse.parse_args()
        dog_type = args["dog_type"]

        return {"dog_type": dog_type}


# Get arguments for /preference endpoint.
user_reqparse = reqparse.RequestParser()
user_reqparse.add_argument(
    "placeholder", type=str, help="This will probably be something real maybe."
)


@api.route("/preference")
@api.expect(user_reqparse)
class FetchUserPreference(Resource):
    def get(self):
        args = dog_reqparse.parse_args()
        placeholder = args["placeholder"]

        return {"placeholder": placeholder}


if __name__ == "__main__":
    app.run(debug=True)
