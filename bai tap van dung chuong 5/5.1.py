import sqlite3

conn = sqlite3.connect('example.db')

print('Phiên bản SQLite là:', sqlite3.version)

conn.close()
