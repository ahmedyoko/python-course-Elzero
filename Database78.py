#............................................................
# Databases => Intro :
#............................................................
# [1] is the place of storing data
# [2] organized into tables (users,categories)
# [3] tables have columns(id,password,username)
# [4] many types of databases(MongoDB,MySQL,SQlite)
# [5] SQL => structure query language
# [6] SQlite => can run in memory or in single file
# [7] you can browse file with ( https://sqlitebrowser.org/)
# [8] data inside DB has types (text,integer,date)
#............................................................
#  connect 
#  execute 
#  close
#............................................................


# # import sqlite module
# import sqlite3

# # create db and connect 
# db = sqlite3.connect("app.db")

# # execute the tables and fields
# db.execute("CREATE TABLE skills(name TEXT,progress INTEGER,user_id INTEGER)") # create table(capital)=> the command ,skill(small)=> the name of table

# # close the db
# db.close()
print('*'*50)
# import sqlite module
import sqlite3

# create db and connect 
db = sqlite3.connect("app.db")

# execute the tables and fields
db.execute("CREATE TABLE if not exists skills(name TEXT,progress INTEGER,user_id INTEGER)") # create table(capital)=> the command ,skill(small)=> the name of table

# close the db
db.close()

print('*'*50)
print('*'*50)


