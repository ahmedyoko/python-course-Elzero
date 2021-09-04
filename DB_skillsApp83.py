#...................................................
# create skills App part 1
#...................................................

# import sqlite3
import sqlite3

# create and connect the db 
db = sqlite3.connect("app.db")

# setting up th cursor to execute all operations
cr = db.cursor()

# My User Id
uid = 1
#  function to use commit and closed method after operations:
def commit_and_closed() :
    """ Commit changes and close database"""
    db.commit() # commit
    db.close()# closed method
    print('Connection To DB Is Closed')


# input large message in variable
input_message = """
What Do You Want To Do?
"s" => show all skills
"a" => append new skill
"d" => delete a skill
"u" => update a skill
"q" => quite the app
choose option :  
"""
# input option choose
user_input = input(input_message).strip().lower()

# print(user_input)

# commands_list
commands_list = ['s','a','d','u','q']

# define the functions
def show_skill() :
    # cr.execute("select * from skills")
    cr.execute(f"select * from skills where user_id = '{uid}' ")
    results = cr.fetchall()
    print(f"you have {len(results)} skills")
    if len(results) > 0 :
        print("showing skills with progress : ")
    for row in results : 
        print(f"skill => {row[0]}" , end=' ')
        print(f"progress => {row[1]}")
    # print("show_skill")
    commit_and_closed()
def add_skill() :
    # print("add_skill")
    sk = input("write a skill name : ").strip().capitalize()
    
    cr.execute(f"select name from skills where name = '{sk}' and user_id = '{uid}' ")
    results = cr.fetchone()
    # print(f"you have {len(results)} skills")
    # print(f"{results}")
    if results == None : # skill is not exist in DB 
        # print(" you can add it : ")
        prog = input("write  skill progress : ").strip()
        # all values must be in single quote , else the name not found error appear
        cr.execute(f"insert into skills(name,progress,user_id) values('{sk}','{prog}','{uid}' )")
    else :
        print(" you can not add it")

        
    
    commit_and_closed()
def delete_skill() :
    sk = input("write a skill name : ").strip().capitalize()
    cr.execute(f"delete from skills where name = '{sk}' and user_id = '{uid}'")  # the value must be in single quote , else the name not found
    # print("delete_skill")
    commit_and_closed()
def update_skill() :
    # print("update_skill")
    sk = input("write a skill name : ").strip().capitalize()
    prog = input("write the new skill progress : ").strip()
    # all values must be in single quote , else the name not found error appear
    cr.execute(f"select * from skills") # this important to fetch before update
    cr.execute(f"update skills set progress ='{prog}' where name = '{sk}' and user_id = '{uid}'")
    commit_and_closed()


# check if the command is exist
if user_input in commands_list :
    print(f'command is found {user_input}')
    if user_input == "s" :
        show_skill()
    elif user_input == "a" :
        add_skill()
    elif user_input == "d" :
        delete_skill()
    elif user_input == "u" :
        update_skill()
    else : 
        print('App Is Closed')
        commit_and_closed()
else : 
    print(f"sorry this command \"{user_input}\" is not found")