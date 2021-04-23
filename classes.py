# Class examples
class Dog:
    def __init__(self, animal_kind, bark):
        self.animal_kind = animal_kind
        self.bark = bark
        self.__is_alive = True

    def set_is_alive(self, alive_status):
        self.__is_alive = alive_status

    def get_is_alive(self):
        return self.__is_alive


bob = Dog("canine", "woof!")

print(bob.animal_kind + ", ", "\n" + bob.bark)

# Doesn't let you access objects/attributes with __
pgrint(bob.__is_alive)

# Using setters and getters though means you can access the hidden objects.
print(Dog.get_is_alive(bob))

