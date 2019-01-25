
"""
CS 521 Information Structures with Python
#########################################
Module          - HW 8
Creation Date   - 11/21/2018
Student Name    - Gautam Gowrishankar

Intent:
    To illustrate class,inheritance,polymorphism.
"""
class Pet:
    kind = "Animal"
    color = "Brown"

    speak_script = "{name} says {sound}"
    str_script = "I am a {kind} named {name}"

    def __init__(self, name):
        self.name = name

    def do_tricks(self):
        print("{name} can do tricks".format(name=self.name))
        self.speak()
        self.hide()

    def speak(self):
        pass

    def hide(self):
        pass


class Jumper:
    #This is a mixin class for hide
    def hide(self):
        print("{name} is hiding".format(name=self.name))


class Dog(Jumper, Pet): # inherit Pet and Jumper class
    kind = "Dog"
    owner = "Leno"

    def __str__(self):
        return ("I am a {kind} named {name}".format(name=self.name, kind=self.kind))

    def __call__(self, action):
        if action == "licking":
            print("{name} is licking".format(name=self.name))
        elif action == "owner":
            print("I am owned by: " + self.owner)


class BigDog(Dog): # inherit Dog
    color = "Grey"
    owner = "Conan"
    spoken_sound = "barf!"

    def __str__(self):
        return ("I am a Big {kind} named {name}".format(name=self.name, kind=self.kind))

    def speak(self):
        print(self.speak_script.format(name=self.name, sound=self.spoken_sound))


class SmallDog(Dog):  # inherit Dog
    spoken_sound = "burr?!"
    owner = "Fallon"
    color = "black"

    def __str__(self):
        return ("I am a Small {kind} named {name}".format(name=self.name, kind=self.kind))

    def speak(self):
        print(self.speak_script.format(name=self.name, sound=self.spoken_sound))


class Cat(Jumper,Pet):# inherit Jumper and Pet base class
    spoken_sound = "Meow"
    kind = "kitten"

    def __str__(self):
        return ("I am just a {kind} named {name}".format(name=self.name, kind=self.kind))

    def speak(self):
        print(self.speak_script.format(name=self.name, sound=self.spoken_sound))

    def climb(self):
        print("{name} is trying to climb the mountain".format(name=self.name))


class HouseCat(Cat): #extending from cat
    spoken_sound = "prrr"
    color = "white"

    def __str__(self):
        return ("I am a house {kind} named {name}".format(name=self.name, kind=self.kind))

    def speak(self):
        print(self.speak_script.format(name=self.name, sound=self.spoken_sound))

def main():
    pet = Pet("Animal")
    dog = Dog("Cookie")
    big_dog = BigDog("Bugs")
    small_dog = SmallDog("Dash")
    cat = Cat("Snowbell")
    house_cat = HouseCat("Peanuts")
    #loop through the class objects
    pets = [pet, dog, big_dog, small_dog, cat, house_cat]

    for pet in pets:
        print(pet.__str__())
        print(pet.kind)
        print(pet.color)
        pet.do_tricks()
        if callable(pet):
            pet("licking")
            pet("owner")
        if "climb" in dir(pet): #check if the function exists
            pet.climb()
        print("________________________")


main()
