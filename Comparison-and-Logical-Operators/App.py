# Comparison
print(3 == 3)
print("dog" == "dog")
print("dog" != "dog")
print("dog" != "cat")
print("dog" == "cat")
print(3 == 3.0)
print(3 == 3.01)

print(2 > 3)
print(2 < 3)
print(2 >= 3)
print(2 <= 3)
print(2 != 3)
print(2 == 3)
print(2 > 3)

# The id function will return a unique identifier for an object
print(id("hi"))
print(id(3))
print(id(3))
print(id(3.0))

# The 'is operator compares to see if both sides are the same object
print(3 is 3.0) # False
print(3 is 3) # True

# Logical Operators
print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False

print(5 > 2 and 4 < 100)    # True
print(5 > 10 and 2 < 100)   # False

print(not True)     # False
print(not False)    # True

x = 10
print(not x == 10)
print(not x == 11)

print(True and True or True and False)
# (True and True) or (True and False)
# True or False
# True
