#sqlite exercise 10/23/17

#make sure to import sqlite
import sqlite3

conn = sqlite3.connect('ages.sqlite')  #if ages doesnt exist, it automatically makes it for you
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Ages')
cur.execute('CREATE TABLE Ages (name VARCHAR, age INTEGER)')

#inserting the names and ages
cur.execute('INSERT INTO Ages (name, age) VALUES (?,?)', ('Kareem', 40))   #the ? is a placeholder, Kareem goes into first ?, 40 into 2nd ?
cur.execute('INSERT INTO Ages (name, age) VALUES (?,?)', ('Oluwademilade', 36))
cur.execute('INSERT INTO Ages (name, age) VALUES (?,?)', ('Aahana', 30))
cur.execute('INSERT INTO Ages (name, age) VALUES (?,?)', ('Ahtasham', 30))
cur.execute('INSERT INTO Ages (name, age) VALUES (?,?)', ('Murry', 26))
cur.execute('INSERT INTO Ages (name, age) VALUES (?,?)', ('Elise', 16))

#selecting
cur.execute('SELECT hex(name || age) AS X FROM Ages ORDER BY X')

conn.commit()
for row in cur:
    print(row)
    break

cur.close()

conn.close()
