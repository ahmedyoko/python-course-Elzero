#.......................................................
# database trainning 
#.......................................................
import sqlite3
from sqlite3.dbapi2 import connect
def get_all_data():


    try:
        # connect to database 
        db = sqlite3.connect("app.db")
        print("the connection to database is succeeded")
        # setting up to the cursor to make all operations
        cr = db.cursor()
        # fetch data from data base 
        cr.execute("select * from users")
        # Assign data to variable
        # results = cr.fetchone()
        results = cr.fetchall()
        print(type(results))
        print(results) # list  of rows its elements in the form of tuple
        print(results[0]) # row of zero
        print(results[1])
        print(f'the number of rows are : {len(results)}')
        # show data 
        print("showing data :")
        # loop on results 
        for row in results :
            print(f'user_id =>{row[0]}',end=" ")
            print(f'user name =>{row[1]}')
    except sqlite3.Error as er :
        print("Error reading data {er}")
    finally :
        if (db) :
            db.close()
            print("connection to database is closed")






get_all_data()


