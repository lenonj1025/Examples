weather = "rainy"

if weather == "sunny":
    print("It is sunny")
    print("Don't bring an umbrella")
elif weather == "rainy":
    print("It is rainy")
    print("Bring an umbrella")
else:
    print("It is not sunny but also not raining")

print("end of program")

# Nested-if statements
gender = input("Are you male or female? ")
age = int(input("What is your age? "))

if gender == "male":
    if (age < 18):
        print("You are a boy")
    else:
        print("You are a man")
elif gender == "female":
    if (age < 18):
        print("You are a girl")
    else:
        print("You are a woman")

