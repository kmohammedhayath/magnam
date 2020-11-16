#!/usr/bin/env python
# coding: utf-8

# In[5]:

#snipet for checking connection
import requests
import json

url = "http://dummy.restapiexample.com/api/v1/employees"

response = requests.get(url)
print(response)
data = response.text
#parsed = json.loads(data)


# In[6]:

#snipet for loading entire data
import requests
import json

url = "http://dummy.restapiexample.com/api/v1/employees"

response = requests.get(url)
print(response)
data = response.text
print(data)


# In[15]:

#snipet for loading all ids of the  data
import requests
import json

url = "http://dummy.restapiexample.com/api/v1/employees"

response = requests.get(url)
print(response)
value = response.text
result = json.loads(value)
for item in result['data']:
    print(item['id'])


# In[16]:

#snipet for loading employee name from data
import requests
import json

url = "http://dummy.restapiexample.com/api/v1/employees"

response = requests.get(url)
print(response)
value = response.text
result = json.loads(value)
for item in result['data']:
    print(item['employee_name'])


# In[ ]:




