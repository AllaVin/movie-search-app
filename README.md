## 🎬 Movie Search App #

### 📋 Table of Contents #

- [🎯 Project Goal](#-project-goal)
- [⚙️ Database Setup](#-database-setup)
- [🛠️ Project Installation](#-project-installation)
- [🖥️ Available Commands](#-available-commands)
- [📚 Usage Examples](#-usage-examples)
- [📂 Project Structure](#-project-structure)
- [🔐 Environment Variables](#-environment-variables)
- [📦 Requirements](#-requirements)
- [👨‍💻 Author](#-author)


### 🎯 Project Goal 
1. Practice working with MySQL databases.
2. Writing SQL queries using Python.
3. Building a console-based interface.
4. Managing a history of user search queries.


### **⚙️ Database Setup**
1. Install MySQL Server
    - [Download MySQL](https://dev.mysql.com/downloads/)
2. Download the Sakila Database Scripts
   - [Official Sakila Page](https://dev.mysql.com/doc/index-other.html)
3. Deploy the Sakila Database:
   - Execute the scripts in order: first sakila-schema.sql, then sakila-data.sql.
4. Create a Database to Store Search History:

```python   
create_db_query = "CREATE DATABASE IF NOT EXISTS group_111124_fp_Alla_Vinogradova"

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
```
5. Configure Connection Settings in db_connection.py:
    - Specify your connection parameters: host, port, username, password, and databases (Sakila, app_db).


### **🛠 Project Installation**

```bash
# Clone the repository
git clone https://github.com/AllaVino/movie-search-app.git 

# Navigate to the project directory
cd Final_Project_Python_Fundamentals

# Install dependencies
pip install -r requirements.txt

# Run application
python main.py
```

### **🔐 Environment Variables**
Create a .env file in the root directory with the following structure:
```env
host_read=your_read_db_host
user_read=your_read_db_user
password_read=your_read_db_password

host_write=your_write_db_host
user_write=your_write_db_user
password_write=your_write_db_password
```
⚠️ Important: Do not share or commit your .env file. Add it to your .gitignore file.

### **🖥️  Available Commands**
| Option number | Description |
|---------------|-------------|
| 1             | Search movie by keyword    |
| 2             | Search movie by genre and year|
| 3             | Show 10 the most popular queries    |
| 4             | Exit    |


### **📚 Usage Examples**
```bash
Please select the option::
1. Search movie by keyword
2. Search movie by genre and year
3. Show 10 the most popular queries
4. Exit
Enter the number of option: 1
Enter the keyword for search: love

Available genres:
1. Action
2. Comedy
...

Select a genre (1-16): 7
Enter the movie release year (1900-2025): 1998

Search results:
+---------------+--------------+------------------------------------------------------------------------------------------------------------------------+
|     Title     | Release year |                                                      Description                                                       |
+---------------+--------------+------------------------------------------------------------------------------------------------------------------------+
|  BLADE POLISH |     1998     | A Thoughtful Character Study of a Frisbee And a Pastry Chef who must Fight a Dentist in The First Manned Space Station |
| SAVANNAH TOWN |     1998     |  A Awe-Inspiring Tale of a Astronaut And a Database Administrator who must Chase a Secret Agent in The Gulf of Mexico  |
+---------------+--------------+------------------------------------------------------------------------------------------------------------------------+

...
```

### **📂 Project Structure**
```bash
project_root/
├── command_handler.py   # Logic for handling user commands
├── db_connection.py     # Database connection setup
├── db_operations.py     # Read/write operations with the database
├── db_setup.py          # Initial database setup
├── display.py           # Console output management
├── main.py              # Application entry point
└── README.md            # Project description
```

### **📦 Requirements**
- [x] Python 3.8+
- [x] MySQL Server
- [x] Library - mysql-connector-python


### **👨‍💻 Author**
Created for educational purposes  
All rights reserved ©