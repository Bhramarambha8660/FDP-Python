class Student:
   def  __init__(self,a,b,c):
      self.id=a
      self.name=b
      self.dept=c
      print('constructor')

   def __str__(self):  # toString() in java
       return f'{self.id}-{self.name}-{self.dept}'

obj=Student(101,'sachin','ece')
print(obj)
