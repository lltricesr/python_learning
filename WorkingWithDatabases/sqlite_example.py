"""
    Basic commands for using the SQLite DB
    import sqlite3 module
"""
import sqlite3
import datetime 

"""
    sqlite3:connect(db_name) -> connects to the sqlite db_name; creates the db_name file if doesn't exist
"""
database = sqlite3.connect("portfolio.db")

"""
    database:cursor -> method to create a cursor; 
    cursor -> required to execute query on the database
"""
cursor = database.cursor()

"""
    building out a query; SQL statement format
    sell INT -> Buy=False/Sell=True; 
        SQLite doesn't have a BOOL type, sqlite3 module handle python bool to sqlite int
    date TIMESTAMP -> SQLite data type for a DATE; sqlite module will convert python DATE to sqlite TIMESTAMP
"""
create_table_query = """
    CREATE TABLE investments (
        coin_id TEXT,
        currency TEXT,
        sell INT,
        amount REAL,
        date TIMESTAMP
    );
"""

"""
    cursor:execute -> method that will perform the SQL query on the DB
"""
cursor.execute(create_table_query)

"""
    performing an investment
    bool:True & datetime:now() -> the python value will be represented with a tuple
"""
investment = ("bitcoin", "usd", True, 1.0, datetime.datetime.now())

"""
    parameterized SQL using ? as placeholders
"""
cursor.execute(
    "INSERT INTO investments VALUES (?, ?, ?, ?, ?);",
    investment
)

"""
    SQL command will not take affect until a commit is performed
"""
database.commit()

"""
    SQL command to retrieve from the DB
    result -> cursor representing the result set from the SQL query
"""
result = cursor.execute("SELECT * FROM investments;")

"""
    (cursor)result:fetchall() -> returns all the rows of data in a list
"""
all_rows = result.fetchall()

"""
    (cursor)result:fetchone() -> returns the first row of data; return None if no rows
"""
first_or_only_row = result.fetchone()