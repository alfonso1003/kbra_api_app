# AddressBook API

## Run the following sequence of commands once to set up the environment:

```
# create virtual environment
cd path/to/project/kbra_api_app
python3 -m venv venv

# activate venv
source venv/bin/activate

# install dependencies
pip3 install -r requirements.txt

# export environment
export FLASK_ENV=development

# create database
python3 manage.py recreate_db

# populate database
python3 manage.py populate_addresses_table
```

## Once environment is built, start the server:

```
# run development server
python3 manage.py run
```
