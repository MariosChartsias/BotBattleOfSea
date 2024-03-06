
import mysql.connector
import json
import numpy as np

class DatabaseHandler(object):

    def __init__(self):
        self.mydb = None
        self.mycursor = None

    def connect2db(self):
        """Connect to database."""
        jsconfigdata = json.load(open('./config_files/config.json'))
        self.mydb = mysql.connector.connect(
            host=jsconfigdata[jsconfigdata["database"]]["host"],
            user=jsconfigdata[jsconfigdata["database"]]["user"],
            port=jsconfigdata[jsconfigdata["database"]]["port"],
            password=jsconfigdata[jsconfigdata["database"]]["password"],
            database=jsconfigdata[jsconfigdata["database"]]["database"]
        )
        self.mycursor = self.mydb.cursor()

    def create_test_table(self):
        """Create a test table."""
        self.connect2db()
        try:
            self.mycursor.execute("CREATE TABLE IF NOT EXISTS `test_table` (ID INT AUTO_INCREMENT PRIMARY KEY, TestData VARCHAR(255))")
            print("Test table created successfully.")
        except mysql.connector.Error as err:
            print(f"Failed to create table: {err}")
        finally:
            self.close_db()

    def close_db(self):
        """Close database connection."""
        if self.mydb.is_connected():
            self.mycursor.close()
            self.mydb.close()
            print("MySQL connection is closed.")