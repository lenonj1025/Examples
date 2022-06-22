from Person import Person

p1 = Person("John", "Doe", 25)
print(p1)

# print(p1.__first_name)
p1.say_hi()

print(p1.get_first_name())
print(p1.get_last_name())
print(p1.get_age())
print(p1.get_fullname())

p1.set_last_name("Tran")
print(p1.get_fullname())
