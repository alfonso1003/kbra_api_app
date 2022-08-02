from flask_restx import Namespace, Resource

api = Namespace("health", description="check the health of the app")


class Health(Resource):
    def get(self):
        return {"status": "OK", "message": "Server is healthy!"}


# empty string means will be at root of namespace
api.add_resource(Health, "")
