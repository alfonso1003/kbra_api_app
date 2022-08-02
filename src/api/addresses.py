from flask import request
from flask_restx import Namespace, Resource, fields
from flask_cors import cross_origin
from src.addresses.services import (
    create_address,
    get_all_addresses,
    get_address,
    update_address,
    delete_address,
)


api = Namespace(
    "addresses",
    description="Address related operations",
    decorators=[cross_origin()],
)


address_fields = api.model(
    "Adress",
    {
        "first_name": fields.String,
        "last_name": fields.String,
        "phone_number": fields.String,
        "email": fields.String,
        "street_address": fields.String,
    },
)


class AddressList(Resource):
    def get(self):
        """Get a list of addresses"""
        return get_all_addresses()

    @api.doc(body=address_fields)
    def post(self):
        """Create a new address"""
        return create_address(request.get_json())


class Address(Resource):
    def get(self, address_id):
        """Get an address by ID"""
        return get_address(address_id)

    @api.doc(body=address_fields)
    def put(self, address_id):
        """Update an address by ID"""
        return update_address(address_id, request.get_json())

    def delete(self, address_id):
        """Delete an address by ID"""
        return delete_address(address_id)


api.add_resource(AddressList, "")
api.add_resource(Address, "/<int:address_id>")
