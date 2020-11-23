#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pymysql

#database connection
connection = pymysql.connect(host="db4free.net",user="kmohammedhayath",passwd="Hayath@123",database="magnamdb" )
cursor = connection.cursor()
# some other statements  with the help of cursor
connection.close()


# In[18]:


import pymysql

#database connection
connection = pymysql.connect(host="db4free.net",user="kmohammedhayath",passwd="Hayath@123",database="magnamdb" )
cursor = connection.cursor()

# queries for inserting values
insert1 = "INSERT INTO Employee (EmployeeID, FirstName, LastName, Email, Address, City) VALUES ('1', 'abhinav', 'suman', 'abhinavsuman21@gmail.com', '#21,attibele mainroad', 'banglore');"


#executing the quires
cursor.execute(insert1)



#commiting the connection then closing it.
connection.commit()
connection.close()


# In[ ]:




