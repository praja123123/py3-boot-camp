# Parent class
class Pets:

    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs

    def if_all_hungry(self):

        # this is result of all dog object hungryness: 'hungry', 'not hungry', 'mixed'
        if self.dogs[0].is_hungry:
            all_hungry = 'hungry'
        else:
            all_hungry = 'not hungry'

        for dog in self.dogs[1:]:
            if dog.is_hungry and all_hungry=='hungry':
                all_hungry = 'hungry'
            elif dog.is_hungry and all_hungry=='not hungry':
                all_hungry = 'mixed'
                break
            elif not dog.is_hungry and all_hungry=='not hungry':
                all_hungry = 'not hungry'
            elif not dog.is_hungry and all_hungry=='hungry':
                all_hungry = 'mixed'
                break

        return all_hungry

    def walk(self):
        for dog in self.dogs:
            print(dog.walk())

# Parent class
class Dog:

    # Class attribute
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age, is_hungry=True):
        self.name = name
        self.age = age
        self.is_hungry = is_hungry

    # Instance method
    def description(self):
        return self.name, self.age

    # Instance method
    def speak(self, sound):
        return "%s says %s" % (self.name, sound)

    # Instance method
    def eat(self):
        self.is_hungry = False

    def walk(self):
        return "{} is walking!".format(self.name)

# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "%s runs %s" % (self.name, speed)


# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "%s runs %s" % (self.name, speed)

# Create instances of dogs
my_dogs = [
    Bulldog("Tom", 6),
    RussellTerrier("Fletcher", 7),
    Dog("Larry", 9)
]

# Instantiate the Pets class
my_pets = Pets(my_dogs)

# Output
print("I have {} dogs.".format(len(my_pets.dogs)))
for dog in my_pets.dogs:
    print("{} is {}.".format(dog.name, dog.age))

print("And they're all {}s, of course.".format(dog.species))

for dog in my_dogs:
    dog.eat()

print('My dogs are {}.'.format(my_pets.if_all_hungry()))

print(my_pets.walk())

print('')
print(my_pets.dogs)
print(Pets.dogs)