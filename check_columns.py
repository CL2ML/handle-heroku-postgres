import os
import psycopg2
import commands
from dotenv import load_dotenv

def check_columns():
    # read connection parameters
    load_dotenv()
    DATABASE_URL = os.environ['DATABASE_URL']
    """ Connect to the PostgreSQL database server """

    conn = None
    try:
        
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
		
        # create a cursor
        cur = conn.cursor()
        
	# execute a statement
        print('PostgreSQL database version:')
        cur.execute(commands.check_table_columns_cmd)

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
       
	    # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    check_columns()


