
import unittest


    
class Employee:  
    def __init__(self, name):  
        
        self.name = name  
  
    def display(self):  
        print(" %s" % (self.name))  
        
  
emp1 = Employee('John')   
  
# accessing display() method to print employee 1 information  
  

 
class TestCalc(unittest.TestCase):
    
    
    
    def test_check(self):
        self.assertEqual(emp1.name, 'John')
    

if __name__ == '__main__':  #it is comulsury to write as it executes all the  testcases
    unittest.main()
