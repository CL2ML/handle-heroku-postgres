# Collection of utility modules to handle a PostgreSQL database on heroku with Python


## General hints

- The heroku Postgres database can be accessed externally by a specific URL provided by the service. The database credentials are changed by heroku from time to time. So, it is advisable to check the URL every time and then to put the it in an environment variable that will be used by the scripts. The databse credentials can be verified here: [data.heroku.com](https://data.heroku.com)
- The database credentials can also be saved into a .env file from which the credentials can be loaded into the environment. Make sure to add a .gitignore file containing '.env'. The package 'dotenv' comes in handy to load variables into the environment from an .env file.
		from dotenv import load_dotenv
		load_dotenv()

## Dependencies

### Py Packages

- psycopg2: PostgreSQL python handler
- dotenv: Load environment variables

### Custom methods

- commands: Custom method containing the SQL commands that will be loaded into the scripts

## Components

- Check database connection
- Create table
- Check tables
- Check table columns

## Sources & Credits

https://data.heroku.com

https://towardsdatascience.com/python-and-postgresql-how-to-access-a-postgresql-database-like-a-data-scientist-b5a9c5a0ea43

https://devcenter.heroku.com/articles/heroku-postgresql#connecting-in-python

https://www.postgresqltutorial.com/postgresql-python/

https://stackabuse.com/working-with-postgresql-in-python/
