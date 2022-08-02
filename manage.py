import faker
from flask.cli import FlaskGroup


from src import create_app, db
from src.addresses.models import Address
# from src.articles.models import Article


app = create_app()


cli = FlaskGroup(create_app=create_app)


@cli.command("recreate_db")
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("populate_addresses_table")
def populate_addresses_table():

    fake = faker.Faker()

    for _ in range(20):

        first_name = fake.first_name()
        last_name = fake.last_name()
        phone_number = fake.phone_number()
        email = fake.email()
        street_address = fake.address().replace("\n", " ")

        address = Address(first_name, last_name, phone_number, email, street_address)
        db.session.add(address)

    db.session.commit()


if __name__ == "__main__":
    cli()
