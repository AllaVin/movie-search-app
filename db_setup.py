from colorama import Fore, Style, init
import os
from pathlib import Path
import dotenv
import mysql.connector

# Initialize Colorama to reset colors automatically after each print
init(autoreset=True)


# Load environment variables from the .env file
dotenv.load_dotenv(Path('.env'))

# Connection settings without specifying a database (used for creating the database itself)
db_config_server = {
    'host': os.environ.get("host_write"),
    'user': os.environ.get("user_write"),
    'password': os.environ.get("password_write")
}

# Connection settings for a specific database (used after the database has been created)
db_config_write = {
    'host': os.environ.get("host_write"),
    'user': os.environ.get("user_write"),
    'password': os.environ.get("password_write"),
    'database': 'group_111124_fp_Alla_Vinogradova'
}

# ------------------------ Step 1: Function to connect and execute a query ------------------------
def execute_query(query, use_app_db=False, commit=False):
    # Select the configuration depending on whether we need the database connection or just the server
    config = db_config_write if use_app_db else db_config_server
    # Establish connection to MySQL server
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    try:
        # Execute the provided SQL query
        cursor.execute(query)
        # Commit changes to the database if required
        if commit:
            conn.commit()
    except mysql.connector.Error as err:
        # Print any SQL execution errors
        print(f"Error: {err}")
    finally:
        # Always close the cursor and connection to avoid leaks
        cursor.close()
        conn.close()

# ------------------------ Step 2: Create the database ------------------------
# SQL query to create a new database if it does not already exist
create_db_query = "CREATE DATABASE IF NOT EXISTS group_111124_fp_Alla_Vinogradova"

# Execute the database creation query (connect without specifying a database)
execute_query(create_db_query)
print(Fore.CYAN + "DB has been successfully created!" + Style.RESET_ALL)

# ------------------------ Step 3: Create the table ------------------------
# SQL query to create the 'search_logs' table to store search records
create_table_query = """
CREATE TABLE IF NOT EXISTS search_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    search_type VARCHAR(50) NOT NULL,
    search_text VARCHAR(255) NOT NULL,
    search_count INT DEFAULT 1,
    search_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(search_type, search_text)
);
"""
# Execute the table creation query while connected to the specific database
execute_query(create_table_query, use_app_db=True, commit=True)
print(Fore.GREEN + "Table 'search_logs' has been successfully created!" + Style.RESET_ALL)