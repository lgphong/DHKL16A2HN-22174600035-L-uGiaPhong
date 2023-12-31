import sqlite3

conn = sqlite3.connect('example.db')

cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Danh sách các bảng là :")
for table in tables:
    print(table[0])

# Đóng kết nối
conn.close()
