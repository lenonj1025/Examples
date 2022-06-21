my_list = [10]  # Creates empty list

# my_list.append adds to list

print(my_list)
print(type(my_list))

print(my_list[0])
print(type(my_list[0]))

my_list.append("abc")
my_list.append(12)
my_list.append(25)
my_list.append("def")

print(my_list)

print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
print(my_list[4])

print(my_list[4 // 2])
a = 3
print(my_list[a])

# Challenge: using a while loop, iterate over and print out each element individually
i = 0
while i < len(my_list):
    print(my_list[i])
    i = i + 1

# Challenge: using a for loop, iterate over  and print out each element individually
for e in my_list:
    print(e)

# Challenge: using a for loop, iterate over and print out the element and index
# Solution 1
index = 0
for e in my_list:
    print(f"{index}: {e}")
    index += 1

# Solution 2 (better)
for idx, e in enumerate(my_list):
    print(f"{idx}: {e}")

# Nested for loops
my_2d_list = [[10, 20], [30, 40]]
print(my_2d_list[0][1])
print(my_2d_list[1][0])
for l in my_2d_list:
    for element in l:
        print(element, end=" ")

# Unpacking
my_list_2 = ['Jace', 'Lenon']
first_name, last_name = my_list_2
print(first_name)
print(last_name)

fruits = ['apple', 'banana', 'peach', 'pear']
# * is used when unpacking to pull all remaining elements into a list
apple, banana, *other_fruits = fruits
print(apple)
print(banana)
print(other_fruits)
print(type(other_fruits))

# Slicing creates a copy of the segment which you are slicing
# Can be used to make a copy of a list
a = [1, 2, 3]
b = a[::]
b[0] = 1000
print(a)
print(b)
