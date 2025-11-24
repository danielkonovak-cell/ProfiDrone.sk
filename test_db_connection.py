import mysql.connector
from mysql.connector import Error

try:
    # Create connection
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='Dae346.daniel@',  # <-- Replace this
        database='why'  # <-- Replace with your database name
    )

    if connection.is_connected():
        print("✅ Connected to MySQL database successfully!")
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print("You are connected to database:", record)

except Error as e:
    print("❌ Error while connecting to MySQL:", e)

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("🔌 MySQL connection closed.")
