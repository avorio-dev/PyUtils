import json

import mysql.connector as mysql


def execute_query(cursor, query):
    print(query)
    try:
        cursor.execute(query)

    except mysql.Error as err:
        print(f"Error MySQL: {err}")

    results = cursor.fetchall()  # Get query results
    for result in results:
        print("\t", result)
    print("\n")


if __name__ == "__main__":
    # Username:
    #   i.e., the username that you use to work with MySQL Server.
    #   The default username for the MySQL database is a root

    # Password:
    #    is given by the user at the time of installing the MySQL database

    # Host Name:
    #   is the server name or Ip address on which MySQL is game_running.
    #   If you are game_running on localhost, then you can use localhost, or it’s IP, i.e. 127.0.0.0

    # Database Name:
    #    name to which you want to connect.

    # Autocommit:
    #   It is enabled by default, you can use it to commit changes on DB automatically.
    #   If false you will need to run db.commit() manually

    with open("MySql_conf.json", "r") as file:
        json_content = json.load(file)

    # Get DBMS Password from input user if not set in JSON
    mysql_conf = json_content['mysql_conf']
    if mysql_conf['dbcon']['passwd'] == "":
        mysql_conf['dbcon']['passwd'] = input("Type login password: \t")

    db = mysql.connect(
        host=mysql_conf['dbcon']['host'],
        user=mysql_conf['dbcon']['user'],
        passwd=mysql_conf['dbcon']['passwd'],
        autocommit=mysql_conf['dbcon']['autocommit']
    )
    print("DB Connector: \t", db)  # it will print a connection object if everything is fine
    print("DB Connected: \t", db.is_connected())

    if db.is_connected():
        db_cursor = db.cursor()

        qShowDB = f"SHOW DATABASES;"
        execute_query(db_cursor, qShowDB)

        qCreateDB = f"CREATE DATABASE IF NOT EXISTS {mysql_conf['database']['database_name']};"
        execute_query(db_cursor, qCreateDB)

        qUseDB = f"USE {mysql_conf['database']['database_name']};"
        execute_query(db_cursor, qUseDB)

        qCreateTable = "CREATE TABLE IF NOT EXISTS People ( Name varchar(50), Age int, City varchar(50) );"
        execute_query(db_cursor, qCreateTable)

        qFillTable = (f"INSERT INTO People (Name, Age, City) VALUES "
                      f"('PyUser', '29', 'Mars'), "
                      f"('PyUser2', '29', 'Mars');")
        execute_query(db_cursor, qFillTable)

        qUpdateTable = f"UPDATE People SET City = 'Moon' WHERE Name = 'PyUser2';"
        execute_query(db_cursor, qUpdateTable)

        qSelectTable = "SELECT * FROM People;"
        execute_query(db_cursor, qSelectTable)

        qDeleteTableContent = "DELETE FROM People;"
        execute_query(db_cursor, qDeleteTableContent)

        qDeleteTable = f"DROP TABLE People;"
        execute_query(db_cursor, qDeleteTable)

        qDeleteDB = f"DROP DATABASE {mysql_conf['database']['database_name']};"
        execute_query(db_cursor, qDeleteDB)

        db_cursor.close()

    db.close()
    print("DB Connected: \t", db.is_connected())
