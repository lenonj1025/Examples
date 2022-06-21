my_tuple = ("adc", 5, True, 10, 25, 1.2)

print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[2])
print(my_tuple[3])
print(my_tuple[4])
print(my_tuple[5])

person_1 = ('Jace', 'Lenon', 24)
first_name, last_name, age = person_1
print(first_name)
print(last_name)
print(age)

# For each iteration, we are unpacking a tuple
for idx, e in enumerate([10, 15, "abc"]):
    print(f"{idx} {e}")

my_tuple_2 = (1, 2, 2, 1, 3, 3, 3, 3, 4, 3, 5, 10)
three_count = my_tuple_2.count(3)
print(f"my_tuple_2 has {three_count} 3's")

print(my_tuple_2.index(5))

# Tuple with only one element, add a comma at the end of the element
my_tuple_3 = (50,)
print(type(my_tuple_3))


