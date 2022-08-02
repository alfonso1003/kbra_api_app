from flask import Blueprint
from flask_restx import Api

from src.api.addresses import api as addresses_ns
from src.api.articles import api as articles_ns
from src.api.health import api as health_ns


api_bp = Blueprint("api", __name__)

api = Api(
    api_bp,
    title="Flask Rest API",
    description="A REST API built with Flask and FlaskRestx",
)

api.add_namespace(addresses_ns)
api.add_namespace(articles_ns)
api.add_namespace(health_ns)
