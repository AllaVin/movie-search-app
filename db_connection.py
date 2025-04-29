import os
from pathlib import Path
import mysql.connector
import dotenv


# Load environment variables from the .env file
dotenv.load_dotenv(Path('.env'))


# Configuration for connecting to the read-only database (sakila)
db_config_read = {
    'host': os.environ.get("host_read"),
    'user': os.environ.get("user_read"),
    'password': os.environ.get("password_read"),
    'database': 'sakila',  # БД для чтения (с фильмами)
}

# Configuration for connecting to the writable database (for logging search queries)
db_config_write = {
    'host': os.environ.get("host_write"),
    'user': os.environ.get("user_write"),
    'password': os.environ.get("password_write"),
    'database': 'group_111124_fp_Alla_Vinogradova',  # БД для записи логов поиска
}

# Function to execute a query against a database
def execute_query(query, use_app_db=False, fetch=False, commit=False, params=None):
    """
    Выполняет запрос к базе данных.

    :param query: SQL-query
    :param use_app_db: if True — use db for logging, else use 'sakila' for reading
    :param fetch: if True — return request result
    :param commit: if True — save changes in db
    :param params: if exist — for adding in request (more securer)
    :return: query result, if fetch=True
    """
    # Select the appropriate database configuration
    config = db_config_write if use_app_db else db_config_read
    # Establish a connection to the database
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    try:
        # Execute the query with parameters if provided (safer way to handle user input)
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        # Commit changes if requested (useful for INSERT/UPDATE/DELETE queries)
        if commit:
            conn.commit()
        # Fetch and return the results if needed (for SELECT queries)
        if fetch:
            return cursor.fetchall()

    except mysql.connector.Error as err:
        # Print an error message if something goes wrong during the database operation
        print(f"Seems that we have connection issue: {err}")

    finally:
        # Always close the cursor and connection, whether or not an error occurred
        cursor.close()
        conn.close()
