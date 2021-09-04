#.......................................................
# database => sqlite => important information
#.......................................................

# import sqlite3
import sqlite3

# create and connect the db 
db = sqlite3.connect("app.db")

# setting up th cursor to execute all operations
cr = db.cursor()

# inserting data
# to prevent db injection :
my_tuple = ('pascal','65',4)
# cr.execute("insert into skills(name,progress,user_id) values('Go','78',2) ")
# cr.execute("insert into skills values('pascal','62',3) ")
cr.execute("insert into skills values(?,?,?) " ,my_tuple) # you can put value of my_tuple
# cr.execute("insert into skills values(?,?,?) " ,('pascal','65',3))

# fetch data from data base
# cr.execute("select * from skills") # into fetch method
# ordered the selection
# cr.execute("select * from skills order by user_id") 
# cr.execute("select * from skills order by user_id desc") 
# cr.execute("select * from skills order by name ") 
# cr.execute("select * from skills order by name desc ") 
# cr.execute("select * from skills order by name limit 2 ") 
# cr.execute("select * from skills order by name limit 5 offset 2 ") #offset : begin after row number 2 
# cr.execute("select * from skills where user_id > 1 ") 
# cr.execute("select * from skills where user_id in (1,3)  ") 
cr.execute("select * from skills where user_id not in (1,2,3)  ") 


# store fetched data in variable 
results = cr.fetchall()

print(len(results))

for row in results :
    print(f"skill name => {row[0]}",end=" ")
    print(f"skill progress => {row[1]}", end=" ")
    print(f"user_id => {row[2]}")

# save the db 
db.commit()

# close the db
db.close()

