"""
database interaction
---------------------
"""
import mysql.connector

conn = mysql.connector.connect(
    user="root",
    password="root",
    host='localhost',
    port=3306,
    database='my_database'
)

"Create Table"
# curs = conn.cursor()
# query = "CREATE TABLE employee (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), age INT)"
# curs.execute(query)
# conn.connect()
# curs.close()
# conn.close()

"insert data"

# curs = conn.cursor()
# query = "INSERT INTO employee (name, age) VALUES(%s, %s)"
# values = ("ramesh", 25)
# curs.execute(query,values)
# conn.commit()
# curs.close()
# conn.close()

"insert multiple"
# curs = conn.cursor()
# query = "INSERT INTO employee (name, age) VALUES(%s, %s)"
# values = [("ganesh", 35), ("suresh", 45), ("harish", 55)]
# curs.executemany(query, values)
# conn.commit()
# curs.close()
# conn.close()


"update data"
# curs = conn.cursor()
# query = "UPDATE employee SET name=%s, age=%s WHERE id=%s"
# values = ("new harish", 50, 4)
# curs.execute(query, values)
# conn.commit()
# curs.close()
# conn.close()

"delete data"
# curs = conn.cursor()
# query = "DELETE FROM employee WHERE id=%s"
# values = (4,)
# curs.execute(query, values)
# conn.commit()
# curs.close()
# conn.close()


"retrieve one row"

# curs = conn.cursor(dictionary=True)
# query = "SELECT * FROM employee WHERE id=%s"
# values = (2,)
# curs.execute(query, values)
# data = curs.fetchone()
# print(data, type(data))
# curs.close()
# conn.close()


"retrieve *"
curs = conn.cursor()
query = "SELECT * FROM employee"
curs.execute(query)
data = curs.fetchall()
print(data, type(data))
curs.close()
conn.close()

