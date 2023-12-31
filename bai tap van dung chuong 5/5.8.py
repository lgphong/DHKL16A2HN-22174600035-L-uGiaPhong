import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute("DELETE FROM example_table WHERE id = ?", (1,))

conn.commit()

conn.close()
