import sqlite3
from typing import Final
def sqlcon():
    global sqliteConnection,cursor
    sqliteConnection=sqlite3.connect("sql.db")
    cursor=sqliteConnection.cursor()

def sqlcreate():
    query="create table Movies(Name varchar(45),Actor varchar(50),Actress varchar(50),Director varchar(50),Year_Of_Release Integer);"
    cursor.execute(query)

def sqlinsert():
    query1="Insert into Movies values('KGF','Yash','Srinidhi','Prashanth','2018');"
    query2="Insert into Movies values('Bad Boys','Will Smith','Theresa','Michael','2014');"
    query3="Insert into Movies values('Joker','Joaquin Phoenix','Sophie','Todd Phillips','2021');"
    query4="Insert into Movies values('Persuit of Happyness','Will Smith','T Newton','Muccino','2006');"
    query5="Insert into Movies values('Independence Day','Will Smith','VA Fox','Roland Emmerich','1976');"
    cursor.execute(query1)
    cursor.execute(query2)
    cursor.execute(query3)
    cursor.execute(query4)
    cursor.execute(query5)
    sqliteConnection.commit()
def sqlselect():
    sqliteConnection=sqlite3.connect("sql.db")
    cursor=sqliteConnection.cursor()
    query1="select * from Movies;"
    query2="select * from Movies where actor='Will Smith';"
    cursor.execute(query1)
    Answer1=cursor.fetchall()   
    cursor.execute(query2)
    Answer2=cursor.fetchall()   
    print(Answer1)
    print(Answer2)
sqlcon()
sqlcreate()
sqlinsert()
sqlselect()
