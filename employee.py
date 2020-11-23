class Employee:
    """A sample Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last
       

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
  
