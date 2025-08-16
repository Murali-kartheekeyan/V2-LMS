import pymysql
import os

def get_db_connection():
    return pymysql.connect(
        host=os.getenv('DB_HOST', 'sql12.freesqldatabase.com'),
        user=os.getenv('DB_USER', 'sql12795106'),
        password=os.getenv('DB_PASSWORD', ' 3kC8zmrVMn'),
        database=os.getenv('DB_NAME', 'sql12795106'),  # <-- UPDATED a
        cursorclass=pymysql.cursors.DictCursor

    )   

