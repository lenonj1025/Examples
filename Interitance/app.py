class Animal:

    def __init__(self, color, number_of_eyes):
        self.color = color
        self.number_of_eyes = number_of_eyes

    def make_noise(self):
        print("**GENERIC ANIMAL NOISE**")

class Dog(Animal):

    def __init__(self, name, color, number_of_eyes):
        super().__init__(color, number_of_eyes)
        # This will call the __init__ method in the parent class and pass in the color argument
        self.name = name

    def play_game(self):
        print(f"{self.name} is playing fetch!")

        # Method overriding
        # Where you replace the implementation of a
        # method inherited from a parent class with the implementation defined in the child class
    def make_noise(self):
        print(f"{self.name} says bark!")


d1 = Dog("Fido", "Blue", 2)
d2 = Dog("Sparky", "Red", 2)
d1.play_game()
d2.play_game()
d1.make_noise()
d2.make_noise()
print(d1.color)
print(d2.color)
print(d1.number_of_eyes)
print(d2.number_of_eyes)

# Overriding is known as runtime polymorphism
choice = input("Enter whether you would like to create an Animal or Dog object ")
d1 = None
if choice == 'Animal':
    d1 = Animal("Black", 2)
elif choice == 'Dog':
    d1 = Dog("Fido", "Black", 2)

d1.make_noise()     # The implementation of make_noise will depend on which object
# the d1 variable is actually referring too
