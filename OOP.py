# 4 Pillars of OOP

# Abstraction - Objects only reveal internal mechanisms that are relevant for the use of other objects. The User is \
# kept unaware as to how the code works. Like a coffee machine you just press the buttons.

# Encapsulation - Hides objects and makes them less accessible to other objects.

# Inheritance - Relationships and subclasses between objects can be assigned. This allows developers to reuse common \
# logic while still maintaining a unique hierarchy. - Reduces development time and ensures a higher level of accuracy.

# Polymorphism - objects can take on more than one form depending on the context.

# ANIMAL CLASS

class Animal:

    # Initialising
    def __init__(self):
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    # Methods
    def breathe(self):
        print('one breathe in and one out')

    def eating(self):
        print('eating sounds')

    def moving(self):
        print('forwards, backwards and side to side')


# Reptile class as a subclass

class Reptile(Animal):

    def __init__(self):
        super().__init__()
        self.cold_blooded = True

    def use_venom(self):
        print('if i have venom i\'m going to use it')

    def moving(self):
        print('moving but as a snake')


bob = Reptile()
cat = Animal()

bob.breathe()
bob.use_venom()
bob.moving()

cat.breathe()
cat.moving()
