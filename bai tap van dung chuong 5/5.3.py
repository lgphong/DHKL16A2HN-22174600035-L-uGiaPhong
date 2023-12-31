import sqlite3
conn = sqlite3.connect('example.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE example_table
                 (id INTEGER PRIMARY KEY,
                  name TEXT,
                  value REAL)''')
conn.commit()
conn.close()
