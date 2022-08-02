from src import db
from src.addresses.models import Address
from src.addresses.schemas import address_schema, address_list_schema
from sqlalchemy import exc


def create_address(data):
    """Given serialized data, deserialize it and create a new address"""
    try:
        address = address_schema.load(data)
        db.session.add(address)
        db.session.commit()
        return address_schema.dump(address), 201
    except exc.IntegrityError:
        db.session.rollback()
        return {
            "message": f"This email ({address.email}) and/or phone number ({address.phone_number}) already exists in the database."
        }, 404


def get_all_addresses():
    """Deserialize and return all addresses in database"""
    return address_list_schema.dump(Address.query.all()), 200


def get_address(address_id):
    """Given an address ID, return a serialized address object"""
    if not (address := Address.query.filter_by(id=address_id).first()):
        return {"message": f"Address with ID {address_id} does not exist"}, 404

    return address_schema.dump(address), 200


def update_address(address_id, data):
    if not (address := Address.query.filter_by(id=address_id).first()):
        return {"message": f"Address with ID {address_id} does not exist"}, 404

    try:
        address_schema.load(data, instance=address, partial=True)
        db.session.commit()
        return address_schema.dump(address), 200
    except exc.IntegrityError:
        db.session.rollback()
        return {
            "message": f"This email ({address.email}) and/or phone number ({address.phone_number}) already exists in the database."
        }, 404


def delete_address(address_id):
    if not (address := Address.query.filter_by(id=address_id).first()):
        return {"message": f"Address with ID {address_id} does exist"}, 404

    db.session.delete(address)
    db.session.commit()
    return "", 204
