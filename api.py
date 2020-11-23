

import requests
import json

url = "http://dummy.restapiexample.com/api/v1/employees"

response = requests.get(url)  #extracts the information from apiendoint that is connected to some database
print(response)  #validates whether connection was successful
data = response.text  #converts jason data into string and load into data variable
#parsed = json.loads(data)

output:
<Response [200]>



import requests
import json

url = "http://dummy.restapiexample.com/api/v1/employees"

response = requests.get(url)
print(response)
value = response.text
print(type(value))
#result = json.loads(value)  # converts jason data in the form of string into python dictonary
#print(result['id'])

output:
<Response [200]>
<class 'str'>




import requests
import json

url = "http://dummy.restapiexample.com/api/v1/employees"

response = requests.get(url)
print(response)
value = response.text
result = json.loads(value)
print(type(result))

output:
<Response [200]>
<class 'dict'>




import requests
import json

url = "http://dummy.restapiexample.com/api/v1/employees"

response = requests.get(url)
print(response)
value = response.text
result = json.loads(value)
print(result['data'])


output:
<Response [200]>
[{'id': '1', 'employee_name': 'Tiger Nixon', 'employee_salary': '320800', 'employee_age': '61', 'profile_image': ''}, {'id': '2', 'employee_name': 'Garrett Winters', 'employee_salary': '170750', 'employee_age': '63', 'profile_image': ''}, {'id': '3', 'employee_name': 'Ashton Cox', 'employee_salary': '86000', 'employee_age': '66', 'profile_image': ''}, {'id': '4', 'employee_name': 'Cedric Kelly', 'employee_salary': '433060', 'employee_age': '22', 'profile_image': ''}, {'id': '5', 'employee_name': 'Airi Satou', 'employee_salary': '162700', 'employee_age': '33', 'profile_image': ''}, {'id': '6', 'employee_name': 'Brielle Williamson', 'employee_salary': '372000', 'employee_age': '61', 'profile_image': ''}, {'id': '7', 'employee_name': 'Herrod Chandler', 'employee_salary': '137500', 'employee_age': '59', 'profile_image': ''}, {'id': '8', 'employee_name': 'Rhona Davidson', 'employee_salary': '327900', 'employee_age': '55', 'profile_image': ''}, {'id': '9', 'employee_name': 'Colleen Hurst', 'employee_salary': '205500', 'employee_age': '39', 'profile_image': ''}, {'id': '10', 'employee_name': 'Sonya Frost', 'employee_salary': '103600', 'employee_age': '23', 'profile_image': ''}, {'id': '11', 'employee_name': 'Jena Gaines', 'employee_salary': '90560', 'employee_age': '30', 'profile_image': ''}, {'id': '12', 'employee_name': 'Quinn Flynn', 'employee_salary': '342000', 'employee_age': '22', 'profile_image': ''}, {'id': '13', 'employee_name': 'Charde Marshall', 'employee_salary': '470600', 'employee_age': '36', 'profile_image': ''}, {'id': '14', 'employee_name': 'Haley Kennedy', 'employee_salary': '313500', 'employee_age': '43', 'profile_image': ''}, {'id': '15', 'employee_name': 'Tatyana Fitzpatrick', 'employee_salary': '385750', 'employee_age': '19', 'profile_image': ''}, {'id': '16', 'employee_name': 'Michael Silva', 'employee_salary': '198500', 'employee_age': '66', 'profile_image': ''}, {'id': '17', 'employee_name': 'Paul Byrd', 'employee_salary': '725000', 'employee_age': '64', 'profile_image': ''}, {'id': '18', 'employee_name': 'Gloria Little', 'employee_salary': '237500', 'employee_age': '59', 'profile_image': ''}, {'id': '19', 'employee_name': 'Bradley Greer', 'employee_salary': '132000', 'employee_age': '41', 'profile_image': ''}, {'id': '20', 'employee_name': 'Dai Rios', 'employee_salary': '21750



import requests
import json

url = "http://dummy.restapiexample.com/api/v1/employees"

response = requests.get(url)
print(response)
value = response.text
result = json.loads(value)
result['data']


output :
<Response [200]>
Out[2]:
[{'id': '1',
  'employee_name': 'Tiger Nixon',
  'employee_salary': '320800',
  'employee_age': '61',
  'profile_image': ''},
 {'id': '2',
  'employee_name': 'Garrett Winters',
  'employee_salary': '170750',
  'employee_age': '63',
  'profile_image': ''},
 {'id': '3',
  'employee_name': 'Ashton Cox',
  'employee_salary': '86000',
  'employee_age': '66',
  'profile_image': ''},
 {'id': '4',
  'employee_name': 'Cedric Kelly',
  'employee_salary': '433060',
  'employee_age': '22',
  'profile_image': ''},
 {'id': '5',
  'employee_name': 'Airi Satou',
  'employee_salary': '162700',
  'employee_age': '33',
  'profile_image': ''},



import requests
import json

url = "http://dummy.restapiexample.com/api/v1/employees"

response = requests.get(url)
print(response)
value = response.text
result = json.loads(value)
for item in result['data']:
    a=item['employee_name']
    b=item['id']
    print(a +" "+b)

output :

<Response [200]>
Tiger Nixon 1
Garrett Winters 2
Ashton Cox 3
Cedric Kelly 4
Airi Satou 5
Brielle Williamson 6
Herrod Chandler 7
Rhona Davidson 8
Colleen Hurst 9
Sonya Frost 10
Jena Gaines 11
Quinn Flynn 12
Charde Marshall 13
Haley Kennedy 14
Tatyana Fitzpatrick 15
Michael Silva 16
Paul Byrd 17
Gloria Little 18
Bradley Greer 19
Dai Rios 20
Jenette Caldwell 21
Yuri Berry 22
Caesar Vance 23
Doris Wilder 24
