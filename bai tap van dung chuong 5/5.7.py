import sqlite3

conn = sqlite3.connect('example.db')

cursor = conn.cursor()

cursor.execute("UPDATE example_table SET column_name = new_value")

conn.commit()

conn.close()
