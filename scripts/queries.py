import sqlite3

conn = sqlite3.connect('pittsburgh.db')

for row in conn.execute('SELECT count(*) from ways_nodes'):
    print row[0]

conn.close()
