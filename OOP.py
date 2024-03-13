class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Goodmorning,my name is {self.name}. I am {self.age} years old. I am {self.gender}.")

person1 = Person("John",22,"male")
person1.introduce()
