## Feedback System API

### Database Setup
* create a file named settings.json and copy data from settings_format.json file
* Set Database name, user, password, port etc
* Run the following command to migrate db
* flask db init (very first time, when no migration is created)
* flask db migrate
* flask db upgrade