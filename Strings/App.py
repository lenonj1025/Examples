a = "This is a string"
b = 'This is another string'

print(a)
print(a[0])
print(a[3])
print(a[0:3])

print(a[-1])
print(a[15])

print(a[-2])
print(a[14])

print(a[0:7:2])

print(a[::-1])
print(a[::2])
print(a[-5:-2])

print(a[-6:])
print(a[0:])
print(a[::])

# String Concatenation
print("Hello " + "World")
num = 10
print("Number: " + str(num))

# String Methods
print("adc".upper())
my_string_1 = "abc"
print(my_string_1.upper())

print("ABC".lower())
my_string_1 = "ABC"
print(my_string_1.lower())

# string() Removes trailing and leading whitespace
a_string = "     asdad      "
print(a_string.strip())

# replace()
my_string_3 = "Hello"
my_string_3 = my_string_3.replace("l", "p")
print(my_string_3)


first_name = "Jace "
last_name = "Lenon "
age = "25"

greeting_message = "Hi, my name is " + first_name + " " + last_name + ", and my age is " + age
print(greeting_message)

greeting_message_2 = "Hi, my name is {} {}, and my age is {}".format(first_name, last_name, age)
print(greeting_message_2)

greeting_message_3 = f"Hi, my name is {first_name} {last_name}, and my age is {age}"
print(greeting_message_3)

# \ is an escape character. It allows for you to escape illegal characters
print("It's a great day!")
print('It\'s a great day!')

print("1st line\n2nd line") # newLine character
print("\tNew paragraph dkdk kdhd dkdk")
print("This is a backslash: \\")

print("a", end=", ")
print("b", end="\n")
print("c")

print("a", "b", "c", sep="\t")

# Length of a string
my_string_4 = "asdddddddddsssssssssssdddddddddddaaaaaaaaaaa"
print(len(my_string_4))

# Occurrence of a character
print(my_string_4.count("a"))

# Find where an occurrence is
print(my_string_4.find("dd"))

