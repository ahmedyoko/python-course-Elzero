#................................................
# DB => sqlite => retrive data from data base
#................................................
# fetchone => return single record or non if no more rows are available
# fetchall => fetch all rows of the query result.It returns all the rows as a list of tuple
#             & an empty list will be returned if no record to fetch
# fetchmany(size) => number of rows
#................................................

# import sqlite3 module
import sqlite3

# create database and connect 
db = sqlite3.connect("app.db")

# setting up the cursor 
cr = db.cursor()
# execute the tables and fields
cr.execute("CREATE TABLE if not exists users(user_id INTEGER,name TEXT)")
cr.execute("CREATE TABLE if not exists skills(name TEXT,progress INTEGER,user_id INTEGER)")

# insert data
cr.execute("insert into users(user_id,name)values(1,'Ahmed')")
cr.execute("insert into users(user_id,name)values(2,'Nagib')")
cr.execute("insert into users(user_id,name)values(3,'Osama')")

# fetch data 
# cr.execute("select name from users")
# cr.execute("select user_id,name from users")
# cr.execute("select * from users")

# print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchall())
# print(cr.fetchmany(2))

# save(commit)changes => to transmit to data base and appear in browser
db.commit()
# close the db
db.close()
print('*'*50)