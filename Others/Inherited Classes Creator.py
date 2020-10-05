class animal:
    def __init__(self, name, color, foots):
        self.name = name
        self.color = color
        self.foots = foots
        print("New animal created!")

    def description(self):
        print("My name is %s, and I'm color %s. I have %d foot." % (self.name, self.color, self.foots))

class dog(animal):
    category = 'Dog'
    def bark(self):
        print("I'm " + self.name + ", a dog: grrrr!")

class cat(animal):
    category = 'Cat'
    def bark(self):
        print("I'm " + self.name + ", a cat: miaauu!")
