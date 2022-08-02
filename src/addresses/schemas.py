from src import ma
from src.addresses.models import Address


class AddressSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Address
        load_instance = True
        ordered = True


address_schema = AddressSchema()
address_list_schema = AddressSchema(many=True)
