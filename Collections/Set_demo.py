my_set_1 = {10, 20}

my_set_2 = set()
print(type(my_set_2))

my_string = "aaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbdddddddccccccccccceeeeeeeee"
# We want to retrieve all the unique characters in the string
for char in my_string:
    my_set_2.add(char)
for char in my_set_2:
    print(char)

my_set_3 = set(my_string)
for char in my_set_3:
    print(char)

# Set Methods
# .add()
# .clear()
# .copy()
# .difference()
# .intersection()
# .union()
# .discard(): remove a specified value (if it exists)
# .pop(): removes a random value from the set

my_set_3 = {1, 2, 3, 4}
my_set_4 = {3, 4, 5, 6}
# intersection does not mutate the sett(creates a new set) intersection.update does mutate the set
print(my_set_3.intersection(my_set_4))
# difference does not mutate the set(creates a new set) difference.update does mutate the set
print(my_set_4.difference(my_set_4))

# Union
print(my_set_3.union(my_set_4))
