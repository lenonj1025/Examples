# One way to populating key-value pairs
person_1 = {}
person_1['first_name'] = "Jace"
person_1['last_name'] = "Lenon"
person_1['age'] = 24

# Another way of pre-populating key-value pairs
person_2 = {'first_name': "Jake", 'last_name': "Doe", 'age': 30}

print(person_1)
print(person_2)

print(person_1['first_name'])
print(person_1['last_name'])
print(person_1['age'])

print(person_2['first_name'])
print(person_2['last_name'])
print(person_2['age'])

my_dict_1 = {
    (10, 20, 30): 'test'
}
print(my_dict_1[(10, 20, 30)])

# Iterating over a dictionary
for k in person_1:
    print(f"{k}: {person_1[k]}")

# .items() returns a list containing a tuple for the key-value pair
for k, v in person_1.items():
    print(f"{k}: {v}")
# person_1.items() -> [('first_name', 'Jace'), ('last_name', 'Lenon'), ('age': 24)}

# .keys() returns a list of keys
for key in person_1.keys():
    print(key)

# .values() returns a list of all the values
for value in person_1.values():
    print(value)

# .pop() to remove a specified key-value pair for a given key
a = person_1.pop('age')
print(a)
print(person_1)

print(person_1['first_name'])
print(person_1.get('first_name'))

# print(person_1['favorite hobby']) # KeyError because the favorite hobby key does not exist
print(person_1.get('favorite_hobby')) #None
print(person_1.get('favorite_hobby'), 'No favorite hobby') # Will be returned if no key favorite hobby is found
