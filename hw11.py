class Vehicle():
    def __init__(self):
        self._make = ''
        self._model = ''
        self._year = ''
        self._mileage = ''
        self._price = ''
    def getMake(self):
        return self._make
    def getModel(self):
        return self._model
    def getYear(self):
        return self._year
    def getMileage(self):
        return self._mileage
    def getPrice(self):
        return self._price
    def changeMake(self,make):
        self._make = make
    def changeModel(self,model):
        self._model = model
    def changeYear(self,year):
        self._year = year
    def changeMileage(self,mileage):
        self._mileage = mileage
    def changePrice(self,price):
        self._price = price

    def Display(self):
        print('Make: ', self._make)
        print('Year: ', self._year)
        print('Model: ',  self._model)
        print('Miles: ', self._mileage)
        print('Price: ', self._price)

class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self._doors = ''
    def getDoors(Self):
        return self._doors
    def changeDoors(self,doors):
        self._doors = doors

    def Display(self):
        super().Display()
        print('Number of doors: ',self._doors)

class Truck(Vehicle):
    def __init__(self):
        super().__init__()
        self._drive = ''
    def getDrive(self):
        return self._drive
    def changeDrive(self,drive):
        self._drive = drive

    def Display(self):
        super().Display()
        print('Drive type: ', self._drive)
        
class SUV(Vehicle):
    def __init__(self):
        super().__init__()
        self._capacity = ''
    def getCapacity(self):
        return self._capacity
    def changeCapacity(self,capacity):
        self._capacity = capacity

    def Display(self):
        super().Display()
        print('Passenger Capacity: ', self._capacity)

class Inventory():
    def __init__(self):
        self._inventory = []
    def addVehicle(self,vehicle):
        self._inventory += [vehicle]
    def Display(self):
        for eachVehicle in self._inventory:
            if type(eachVehicle) == Car:
                print('Inventory unit: Car')
            elif type(eachVehicle) == Truck:
                print('Inventory unit: Truck')
            elif type(eachVehicle) == SUV:
                print('Inventory unit: SUV')
            else:
                print('Inventory unit: Vehicle')
                
            eachVehicle.Display()

def main():
    a = '.'
    inventory = Inventory()
    while a != '':
        a = str(input('Car, truck, or SUV? (Enter to end): '))
        a = a.lower()
        if a == 'car':
            c = Car()
            make = str(input('Enter make: '))
            c.changeMake(make)
            year = str(input('Enter year: '))
            c.changeYear(year)
            model = str(input('Enter model: '))
            c.changeModel(model)
            miles = str(input('Enter mileage: '))
            c.changeMileage(miles)
            price = str(input('Enter price: '))
            c.changePrice(price)
            doors = str(input('Enter number of doors: '))
            c.changeDoors(doors)
            inventory.addVehicle(c)
        elif a == 'truck':
            t = Truck()
            make = str(input('Enter make: '))
            t.changeMake(make)
            year = str(input('Enter year: '))
            t.changeYear(year)
            model = str(input('Enter model: '))
            t.changeModel(model)
            miles = str(input('Enter mileage: '))
            t.changeMileage(miles)
            price = str(input('Enter price: '))
            t.changePrice(price)
            drive = str(input('Enter drive type: '))
            t.changeDrive(drive)
            inventory.addVehicle(t)
        elif a == 'suv':
            s = SUV()
            make = str(input('Enter make: '))
            s.changeMake(make)
            year = str(input('Enter year: '))
            s.changeYear(year)
            model = str(input('Enter model: '))
            s.changeModel(model)
            miles = str(input('Enter mileage: '))
            s.changeMileage(miles)
            price = str(input('Enter price: '))
            s.changePrice(price)
            capacity = str(input('Enter passenger capacity: '))
            s.changeCapacity(capacity)
            inventory.addVehicle(s)
        else:
            a = ''
    inventory.Display()
