from person import Person

p1 = Person("Bach", "Tran", 24)
print(p1)

p2 = Person("John", "Doe", 25)
print(p2)

print(len([1, 2, 3]))
print(len("a string"))

print(len(p1))
print(len(p2))

print("Bach" in p1) # The in operator can be used via defining what it means for something to be "in" the object
# Defined via the __contains__(self, name) method
