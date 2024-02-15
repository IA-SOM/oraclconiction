import os
import cx_Oracle

def conect():

    # Store credentials in environment variables (recommended)
    os.environ['ORACLE_USER'] = 'samir'
    os.environ['ORACLE_PASSWORD'] = 'samir'
    os.environ['ORACLE_HOST'] = 'oracle'  # Use container IP

    print(os.environ['ORACLE_USER'])

    # Alternatively, use hardcoded credentials (not recommended for production)
    user = os.environ['ORACLE_USER'] if 'ORACLE_USER' in os.environ else 'sysdba'

    password = os.environ['ORACLE_PASSWORD'] if 'ORACLE_PASSWORD' in os.environ else 'samir5636123'
    host = os.environ['ORACLE_HOST'] if 'ORACLE_HOST' in os.environ else 'oracle'
    port = 1521
    sid = 'FREE'

    print(host)

    try:
        dsn = cx_Oracle.makedsn(host, port, sid)
        with cx_Oracle.connect(user, password, dsn) as con:
            cursor = con.cursor()

            cursor.close()
        print("connected ")
    except cx_Oracle.DatabaseError as e:
        print("Error connecting to Oracle database:", e)