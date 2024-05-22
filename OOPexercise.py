class Dog:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

dawa = Dog("Layla", "Golden", 3)
nima = Dog("Kuma", "Brown", 2)
blacky = Dog("Henry", "White", 4)

print(nima.name, nima.color, nima.age)
print(dawa.name, dawa.color, dawa.age)
print(blacky.name, blacky.color, blacky.age)