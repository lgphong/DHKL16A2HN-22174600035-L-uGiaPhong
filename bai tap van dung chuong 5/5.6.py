import sqlite3

conn = sqlite3.connect('example.db')

cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM example_table")
record_count = cursor.fetchone()[0]

print("Số bản ghi trong bảng là : \n" ,record_count)

conn.close()
