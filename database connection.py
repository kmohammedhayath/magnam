#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#install pyodbc module by typing    > "pip install pyodbc"  in command prompt
import pyodbc

def read(connection):
    print("read")
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM EMP ")
    rows=cursor.fetchone()
    for row in rows:
    print(row)
    print()
    
def create(connection):
    print("create")
    cursor=connection.cursor()
    cursor.execute("CREATE TABLE EMP(name varchar(200), salary int (200)) ")
    read(connection)
    
def insert(connection):
    print("insert")
    cursor=connection.cursor()
    sqlform ="INSERT INTO  EMP (name,val) VALUES (%s,%s)"  #inserting values in multiple rows
    employees =[("harshit",1000),("raj",2000),("monu",3000)]
    cursor.executemany(sqlform,employee)
    cursor.commit()
    read(connection)
    
def update(connection):
    print("update")
    cursor=connection.cursor()
    cursor.execute("UPDATE EMP SET salary=7000 WHERE name='ankit' ")
    cursor.commit()
    read(connection)    
        
def delete(connection):
    print("delete")
    cursor=connection.cursor()
    cursor.execute("DELETE FROM EMP WHERE name='harshit' ")
    cursor.commit()
    read(connection)    
    
    
connection= pyodbc.connect('DRIVER={SQL Server Native client 11.0};SERVER=.sql2016;DATABASE=sample;UID=root;PWD=123')


read(connection)
create(connection)
insert(connection)
update(connection)
delete(connection)

cursor.close()


# In[ ]:


#install pyodbc module by typing    > "pip install pyodbc"  in command prompt
import pyodbc
connection= pyodbc.connect('DRIVER={SQL Server Native client 11.0};SERVER=.sql2016;DATABASE=sample;UID=root;PWD=123')
cursor=connection.cursor() #create cursor object to execute a query
cursor.execute("SELECT * FROM EMP") #writing query to perform operation
rows=cursor.fetchall() #fetches all the records or row from emp table and load in variable rows
rows=cursor.fetchone()
for row in rows:
    print(row) #fetches all rows
    print(row[1]) #fetches 2nd column from emp table
    
    


# In[ ]:


#install pyodbc module by typing    > "pip install pyodbc"  in command prompt
import pyodbc
connection= pyodbc.connect('DRIVER={SQL Server Native client 11.0};SERVER=.sql2016;DATABASE=sample;UID=root;PWD=123')
cursor=connection.cursor() #create cursor object to execute a query
cursor.execute("INSERT INTO EMP VALUES(2000,'MIKE','234567','mike123@gmail.com')") #inserting values into the table

sqlform ="INSERT INTO  EMP (name,val) VALUES (%s,%s)"  #inserting values in multiple rows
employees =[("harshit",1000),("raj",2000),("monu",3000)]
cursor.executemany(sqlform,employee)

cursor.commit()
cursor.close()

