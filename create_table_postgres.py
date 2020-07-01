import os
import psycopg2
import commands
from dotenv import load_dotenv

def create_tables():
    """ create tables in the PostgreSQL database"""

    conn = None
    try:
        # read the connection parameters
        load_dotenv()
        DATABASE_URL = os.environ['DATABASE_URL']
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        cur = conn.cursor()
        print('Connected')
        # create table
        cur.execute(commands.create_table_cmd)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()
