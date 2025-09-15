from db_config import get_connection

conn = get_connection()
if conn:
    print("✅ Connection successful!")
    cursor = conn.cursor()
    cursor.execute("SELECT DATABASE();")
    record = cursor.fetchone()
    print("Connected to database:", record)
    conn.close()
else:
    print("❌ Connection failed.")
