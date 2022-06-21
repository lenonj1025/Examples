# Challenge: print out the #'s from 1 to 100

# While Loop
num = 1
while num <= 100:
    print(num, end=", ")
    num = num + 1
print()


# For Loop
# range is known as an iterable(can iterate over that object)
print(type(range(1, 101)))

for num in range(1, 101):
    print(num, end=", ")
print()


# Challenge: print out multiples of 3 from 0 to 100
for num in range(0, 100, 3):
    print(num, end=", ")
print()


# Challenge: print out the first 10 numbers
for num in range(10):
    print(num, end=", ")
print()


# Challenge: print out numbers from 10 to 1 in revers
for num in range(10, 0, -1):
    print(num)

# Challenge: print out hello 1000 times
for _ in range(1000):
    print("hello", end=" ")
print()

# Challenge: print out the characters in a string one by one
for char in "hello":
    print(char)


# break
while True:
    print("Welcome to the calculator app ")
    num1 = int(input("Enter the first number you would like to add: "))
    num2 = int(input("Enter the second number you would like to add: "))

    result = (num1 + num2)
    print(f"The result of {num1} + {num2} is {result}")

    should_continue = input("Would you like to continue? (Y/N): ")
    if should_continue.upper() == 'N':
        break
