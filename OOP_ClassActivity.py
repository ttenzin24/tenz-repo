class dog:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

dog1= dog("Layla","Golden",3)
dog2= dog("Kumu","Hazel Brown",4)
dog3= dog("Bam","Black",5)

print(f"Name: {dog1.name}, Color: {dog1.color}, Age: {dog1.age}")
print(f"Name: {dog2.name}, Color: {dog2.color}, Age: {dog2.age}")
print(f"Name: {dog3.name}, Color: {dog3.color}, Age: {dog3.age}")
