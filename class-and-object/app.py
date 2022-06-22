# Python has many built-in types
# Everything in Python is also considered an object
# int
# float
# str
# list
# set
# dict
# tuple
# range
# bool

# You can define your own types in Python using classes
# and create objects based on those classes

class Person:

    # __init__() is a type of "dunder" method
    # "dunder" --> double underscore
    # in Particular, the purpose of __init__() is to initially populate values for a Person object that is
    # being initialized

    def __init__(self, first_name, last_name, age):
        # self refers to the "current" object
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def say_hi(self):
        print(f"Hi, my name is {self.first_name} {self.last_name}, and I am {self.age} years old")

    def have_birthday_party(self):
        print("Hooray, today is my birthday")
        self.age += 1


# Object creation/instantiation/initialization/construction
# Objects can also be referred to as an "instance"
# An "instance of Person" is the same as a "Person object"

p1 = Person("John", 'Doe', 30)
p2 = Person("Jane", "Doe", 25)
p3 = Person("Bach", "Tran", 24)

print(type(p1))
print(type(p2))
print(type(p3))

print(p1.first_name)
print(p2.first_name)
print(p3.first_name)

print(p1.last_name)
print(p2.last_name)
print(p3.last_name)

p1.say_hi()
p2.say_hi()
p3.say_hi()

p1.have_birthday_party()
p1.say_hi()
p2.say_hi()
p3.say_hi()

# You can actually call the instance methods by referring to the class itself (Person)
# But you still need to provide an object that "self" can refer to
Person.say_hi(p1)
Person.say_hi(p2)
Person.say_hi(p3)

class Todos:
    def __init__(self, description):
        self.description = description
        self.completed = False


class User:
    def __init__(self, username, mobile_phone):
        self.username = username
        self.mobile_phone = mobile_phone
        self.todos = []


user1 = User("lenonj", "001-001-0001")

todo1 = Todos("Sweep floor")
user1.todos.append(todo1)

user1.todos.append(Todos("Make bed"))

print(user1.todos)
