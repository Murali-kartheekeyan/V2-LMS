import psycopg2
import os

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv('DB_HOST', 'dpg-d35tb3ndiees738kb2i0-a.singapore-postgres.render.com'),
        user=os.getenv('DB_USER', 'new_ekjw_user'),
        password=os.getenv('DB_PASSWORD', 'iS15JOBw5cpgAZHHAraVGSZyREb9rv2d'),
        database=os.getenv('DB_NAME', 'new_ekjw'),
        cursor_factory=psycopg2.extras.DictCursor
    )
