import mysql.connector


def count_ID(table):
    # connecting to server
    con = mysql.connector.connect(
  host="sql6.freesqldatabase.com",
  user="sql6478428",
  password="**********",
  database = "sql6478428"
)
    # making command executer
    cursor = con.cursor()
    # making the command
    command = "SELECT count(ID) FROM " + table
    # runing the command
    cursor.execute(command)
    # making data readabla
    data = []
    row = cursor.fetchone()
    while row:
        for i in row:
            data.append(i)
        row = cursor.fetchone()
    # closing conection
    con.close()
    #returning
    return data[0]+1
def signup(values):
    #connecting to server
    con = mysql.connector.connect(
  host="sql6.freesqldatabase.com",
  user="sql6478428",
  password="**********",
  database = "sql6478428"
)
    #making command executer
    cursor = con.cursor()
    #making the command
    ID = str(count_ID('Users'))
    command = "insert into "+'Users'+" VALUES("+ID+','
    for i in range(len(values)-1):
        if type(values[i]) == str:
            command += "'"
        command += str(values[i])
        if type(values[i]) == str:
            command += "'"
        command+= " , "
    if type(values[-1]) == str:
        command += "'"
    command += values[-1]
    if type(values[-1]) == str:
            command += "'"
    command += ")"
    #runing the command
    cursor.execute(command)   
    #making a data for user
    #making the command
    command = "insert into UserXP VALUES("+ID+', 0 , 1)'
    #runing the command
    cursor.execute(command)
    #saving changes
    con.commit()
    #closing conection
    con.close()

def insert(values, table):
    # connecting to server
    con = mysql.connector.connect(
  host="sql6.freesqldatabase.com",
  user="sql6478428",
  password="**********",
  database = "sql6478428"
)
    # making command executer
    cursor = con.cursor()
    # making the command
    ID = str(count_ID('Users'))
    command = "insert into " + table + " VALUES("
    for i in range(len(values) - 1):
        if type(values[i]) == str:
            command += "'"
        command += str(values[i])
        if type(values[i]) == str:
            command += "'"
        command += " , "
    if type(values[-1]) == str:
        command += "'"
    command += str(values[-1])
    if type(values[-1]) == str:
        command += "'"
    command += ")"
    #runing the command
    print(command)
    cursor.execute(command)   
    # saving changes
    con.commit()
    # closing conection
    con.close()


def select(ID, table, info = '*',condition = 'ID'):
    ID = str(ID)
    # connecting to server
    con = mysql.connector.connect(
  host="sql6.freesqldatabase.com",
  user="sql6478428",
  password="**********",
  database = "sql6478428"
)
    # making command executer
    cursor = con.cursor()
    # making the command
    command = "SELECT " + info + " FROM " + table + " WHERE "+condition+" = " + ID
    # runing the command
    cursor.execute(command)
    # making the data readable
    data = []
    row = cursor.fetchone()
    while row:
        line = []
        for i in row:
            line.append(i)
        data.append(line)
        row = cursor.fetchone()
    # closing conection
    con.close()
    # returning
    return data
def delete(ID):
    ID = str(ID)
    #connecting to server
    con = mysql.connector.connect(
  host="sql6.freesqldatabase.com",
  user="sql6478428",
  password="**********",
  database = "sql6478428"
)
    #making command executer
    cursor = con.cursor()
    #making the command
    command = "DELETE FROM Users WHERE ID = "+ID
    #runing the command
    cursor.execute(command)
    #making the command
    command = "DELETE FROM UserXP WHERE ID = "+ID
    #runing the command
    cursor.execute(command)
    #saving changes
    con.commit()
    #closing conection
    con.close()
def update(id,xp):
    #connecting to server
    con = mysql.connector.connect(
  host="sql6.freesqldatabase.com",
  user="sql6478428",
  password="**********",
  database = "sql6478428"
    )
    id = str(id)
    xp = str(xp)
    #connecting to server
    user_level = (select(id, 'UserXP', 'UserLevel'))[0][0]
    if user_level == 0:
        user_level = 1
    needed_xp = (select(user_level, 'Levels', 'NeededXP','Level'))[0][0]
    user_xp = (select(id, 'UserXP', 'XP'))[0][0]
    new_xp = int(user_xp)+int(xp)
    if new_xp >= needed_xp:
        user_level += 1
        new_xp %= needed_xp
    # making command executer
    cursor = con.cursor()
    # making the command
    command = "update UserXP SET UserLevel = "+str(user_level)+" , XP = "+str(new_xp)+" where ID = "+str(id)
    # runing the command
    cursor.execute(command)
    #saving changes
    con.commit()
    #closing conection
    con.close()
    