import sqlite3
conn = sqlite3.connect('example.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE example_table
                 (id INTEGER PRIMARY KEY,
                  name TEXT,
                  value REAL)''')

cursor.execute("INSERT INTO example_table (name, value) VALUES ('apple', 1.23)")
cursor.execute("INSERT INTO example_table (name, value) VALUES ('banana', 4.56)")
cursor.execute("INSERT INTO example_table (name, value) VALUES ('cherry', 7.89)")

cursor.execute("SELECT * FROM example_table")
rows = cursor.fetchall()

# In ra các bản ghi
print("Các bản ghi trong bảng là :")
for row in rows:
    print(row)

# Đóng kết nối
conn.close()
