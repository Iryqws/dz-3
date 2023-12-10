class Human:
    def __init__(self, name="Human"):
        self.name = name

class Animal:
    def __init__(self, name="Animal"):
        self.name = name

class Model:
    def __init__(self, name="Model"):
        self.name = name

class Auto1:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

        def __add_passenger__(self, human):
            self.passengers.append(human) 

        def __print_passengers_names__(self):
            if self.passengers!= []:
                print(f"Names of {self.brand} passengers:")
            for passengers in self.passengers:
                print(passengers.name)
            else:
                print(f"There are on passengers in {self.brand}")

class Auto2:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

        def __add_passenger__(self, human):
            self.passengers.append(human) 

        def __print_passengers_names__(self):
            if self.passengers!= []:
                print(f"Names of {self.brand} passengers:")
            for passenger in self.passengers:
                print(passenger.name)
            else:
                print(f"There are on passengers in {self.brand}")


nick = Human("Nick")
kate = Human("Kate")
tom = Human("Tom")
jane = Human("Jane")

q8 = Model("Audi Q8 model")
m5 = Model("BMW m5 model")

dog = Animal("dog")
cat = Animal("cat")

car1 = Auto1("BMW")
car2 = Auto2("Audi")

car1.add_animal(dog)
car1.add_passenger(nick)
car1.add_passenger(kate)
car2.add_passenger(jane)
car2.add_passenger(tom)
car2.add_animal(cat)
car1.add_model(q8)
car2.add_model(m5)



car1.print_passengers_names()
car2.print_passengers_names()
car1.print_animal_names()
car2.print_animal_names()
car1.print_model_names()
car2.print_model_names()