import pyodbc
def insert(column,values,table):
    #connecting to server
    con = pyodbc.connect('DRIVER={SQL Server}; SERVER=DESKTOP-UT46DSN; Database=Sudoku; UID=sa; PWD=1234;')
    #making command executer
    cursor = con.cursor()
    #making the command 
    command = "insert into "+table+" ("
    for i in range (len(column)-1):
        command += column[i]+" , "
    command += column[-1]+") values ("
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
    #making the data readable and returning it
    data = cursor.fetchall()
    return data
    #closing conection
    con.close()
