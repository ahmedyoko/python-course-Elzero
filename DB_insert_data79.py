# insert data into db
#............................................................
# cursor => all operation in sql done by cursor not by the connection itself
# commit => save all changes
#............................................................
# import sqlite module
# import sqlite3

# # create db and connect 
# db = sqlite3.connect("app.db")


# # setting up the cursor 
# cr = db.cursor()
# # execute the tables and fields
# cr.execute("CREATE TABLE if not exists users(user_id INTEGER,name TEXT)")
# cr.execute("CREATE TABLE if not exists skills(name TEXT,progress INTEGER,user_id INTEGER)")

# # insert data
# cr.execute("insert into users(user_id,name)values(1,'Ahmed')")
# cr.execute("insert into users(user_id,name)values(2,'Nagib')")
# cr.execute("insert into users(user_id,name)values(3,'Osama')")

# # save(commit)changes => to transmit to data base and appear in browser
# db.commit()
# # close the db
# db.close()
print('*'*50)
# delete db and make it again with for loop
import sqlite3

# create db and connect 
db = sqlite3.connect("app.db")


# setting up the cursor 
cr = db.cursor()
# execute the tables and fields
cr.execute("CREATE TABLE if not exists users(user_id INTEGER,name TEXT)")
cr.execute("CREATE TABLE if not exists skills(name TEXT,progress INTEGER,user_id INTEGER)")

# insert data
# cr.execute("insert into users(user_id,name)values(1,'Ahmed')")
# cr.execute("insert into users(user_id,name)values(2,'Nagib')")
# cr.execute("insert into users(user_id,name)values(3,'Osama')")
my_list = ["Ahmed","Osama","Maged","tharwat","wael","waleed","Mohammed","Aadel"]
for key,user in enumerate(my_list) :
    cr.execute(f"insert into users(user_id,name)values({key+1},'{user}')")

# save(commit)changes => to transmit to data base and appear in browser
db.commit()
# close the db
db.close()