class MyClass:
  x = 5


p1 = MyClass()
print(p1.x)

#class 2

class Person:
  def __init__(self, name, age):  #Constructor
    self.name = name
    self.age = age

#Objects
p2 = Person('Jon', 87)
print(p2.name)
print(p2.age)

name = input("Enter Your Name: ")
age = int(input("Enter your age: "))
p3 = Person(name, age)
print(p3.name)
print(p3.age)

class Abc:
  pass    #to make an empty class
     