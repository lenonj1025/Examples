from Animal import Animal

class Dog(Animal):

    def __init__(self, name, num_of_legs):
        super().__init__(num_of_legs)
        self.__name = name

    def make_noise(self):
        print(f"{self.__name}Bark!")

    def get_name(self):
        return self.__name

    def set_name(self):
        self.__name = name
