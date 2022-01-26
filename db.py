import pyodbc
def count_ID(table):
    #connecting to server
    con = pyodbc.connect('DRIVER={SQL Server}; SERVER=DESKTOP-UT46DSN; Database=Sudoku; UID=sa; PWD=1234;')
    #making command executer
    cursor = con.cursor()
    #making the command
    command = "SELECT count(ID) FROM "+table
    #runing the command
    cursor.execute(command)
    #making data readabla
    data = []
    row = cursor.fetchone() 
    while row: 
        for i in row:
            data.append(i)
        row = cursor.fetchone()
    #closing conection
    con.close()
    #returning
    return data[0]+1
    
    

def insert(values,table):
    #connecting to server
    con = pyodbc.connect('DRIVER={SQL Server}; SERVER=DESKTOP-UT46DSN; Database=Sudoku; UID=sa; PWD=1234;')
    #making command executer
    cursor = con.cursor()
    #making the command
    ID = str(count_ID('Users'))
    command = "insert into "+table+" VALUES("+ID+','
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
    #saving changes
    con.commit()
    #closing conection
    con.close()
def select(ID,table,info):
    #connecting to server
    con = pyodbc.connect('DRIVER={SQL Server}; SERVER=DESKTOP-UT46DSN; Database=Sudoku; UID=sa; PWD=1234;')
    #making command executer
    cursor = con.cursor()
    #making the command
    command = "SELECT "+info+" FROM "+table+" WHERE ID = "+ID
    #runing the command
    cursor.execute(command)
    #making the data readable
    data = []
    row = cursor.fetchone() 
    while row:
        line = []
        for i in row:
            line.append(i)
        data.append(line)
        row = cursor.fetchone()
    #closing conection
    con.close()
    #returning
    return data
def delete(table , ID):
    #connecting to server
    con = pyodbc.connect('DRIVER={SQL Server}; SERVER=DESKTOP-UT46DSN; Database=Sudoku; UID=sa; PWD=1234;')
    #making command executer
    cursor = con.cursor()
    #making the command
    command = "DELETE FROM "+table+" WHERE ID = "+ID
    #runing the command
    cursor.execute(command)
    #saving changes
    con.commit()
    #closing conection
    con.close()
