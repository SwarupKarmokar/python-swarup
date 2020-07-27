# object oriented programming:
# objects: in python everything is an object.
print(type(1))
print(type(1.4))
print(type([]))
print(type(()))
print(type({}))
# all the things are called objects.

# class: user defined object are created using class keyword.
# as of now we think that the "class" keyword is a blueprint that defines nature of future objects
# from classes we can create instances
# instances: instance is a specific object created from a particular class.

# creating a class:
class Hello:  # class name starts with capital later
    pass  # this called attribute
# creating instance:
x = Hello()
print(type(x))  # here x is the instance of hello class(you can think instances is the nick name of classes)

# attributes:
# an attribute is a characteristic of an object(assume dog is the object so the attributes be the dog's name, breed')
class Dog:
    def __init__(self,name,breed):  # its called methods( an operation where we define our attributes and perform some stuff)
        self.name = name
        self.breed = breed # both are attributes
# creating instance:
x = Dog(name='kalu', breed='Lab')
# now if we want to know the dog name and breed we can use-->
print(x.name)
print(x.breed)

# class object attributes:
class Dog:
    # Class Object Attribute
    species = 'mammal'

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name
sam = Dog(breed='Lab', name='Sam')
print(sam.breed)
print(sam.name)
print(sam.species)  # its print class object attributes


# Inheritance
# Inheritance is a way to form new classes using classes that have already been defined.
# The newly formed classes are called derived classes, the classes that we derive from are called base classes.
# Important benefits of inheritance are code reuse and reduction of complexity of a program.
# The derived classes (descendants) override or extend the functionality of base classes (ancestors).
#
# Let's see an example by incorporating our previous work on the Dog class:
class Animal:
    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self) # inherit the animal class
        print("Dog created")

    def whoAmI(self):
        print("Dog")

    def bark(self):
        print("Woof!")

d = Dog()
# print(d)
print(d.eat())
print(d.whoAmI())
print(d.bark())

# Polymorphism:
# polymorphism refers the way in which different objects classes can share the same method name..
class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says Woof!'


class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says Meow!'


niko = Dog('Niko')
felix = Cat('Felix')

print(niko.speak())
print(felix.speak())







