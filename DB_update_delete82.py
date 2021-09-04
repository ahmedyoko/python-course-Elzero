#...................................................
# DB => update and delete
#...................................................
# import sqlite3
import sqlite3

db = sqlite3.connect("app.db")

# cursor to make all operations
cr = db.cursor()

# update data 
cr.execute("update users set name = 'Gamal' where user_id = 1") 
cr.execute("update users set name = 'Mahmoud' where user_id =2") 
# cr.execute("update users set name = 'Amer' where user_id = 3") 

# # Delete users
cr.execute("delete from users")

# fetch data 
cr.execute('select * from users')
print(cr.fetchone())
print(cr.fetchone())
print(cr.fetchone())

# save to update=> without it all execution not appear in db
db.commit
# close the db
db.close()