import sqlite3

def convert(value):
    if value.startswith('~'):
        value=value.rstrip('~\n')
        value = value.lstrip('~')
        return value
    if not value:
        value = '0'
        return float(value)

conn = sqlite3.connect('test.db')
curs = conn.cursor()
curs.execute('''
CREATE TABLE food (
 id TEXT , 
 num TEXT, 
 label TEXT) 
''')
query = 'INSERT INTO food VALUES (?,?,?)'
field_count = 4
for line in open('DATSRCLN.txt'):
    fields = line.split('^')
    print(fields)
    vals = [convert(f) for f in fields[:field_count]]
    curs.execute(query, vals)

conn.commit()
conn.close()