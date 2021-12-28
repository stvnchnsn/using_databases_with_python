import sqlite3

conn = sqlite3.connect('quiz_test.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Ages''')

conn.execute('''CREATE TABLE Ages ( 
  name VARCHAR(128), 
  age INTEGER
)''')
conn.commit()
cur.execute('''DELETE FROM Ages''')
cur.execute("INSERT INTO Ages (name, age) VALUES ('Ivory', 15)")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Erika', 19)")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Tyllor', 31)")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Ogheneochuko', 31)")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Ruta', 16)")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Jaden', 21)")
conn.commit()
sqlstr = '''SELECT hex(name || age) AS X FROM Ages ORDER BY X'''

for row in cur.execute(sqlstr):
    print(str(row[0]))


conn.commit()
