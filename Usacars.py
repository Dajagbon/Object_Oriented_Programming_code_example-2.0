import pandas as pd

# Define the Car class
class Car:
    def __init__(self, manufacturer, model, year, mileage, engine, transmission, drivetrain, mpg, exterior_color, interior_color, accidents_or_damage, price):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.mileage = mileage
        self.engine = engine
        self.transmission = transmission
        self.drivetrain = drivetrain
        self.mpg = mpg
        self.exterior_color = exterior_color
        self.interior_color = interior_color
        self.accidents_or_damage = accidents_or_damage
        self.price = price

    def Paint(self, color):
        self.exterior_color = color
        print(f"The car has been painted {color}.")

    def Repair(self, part, replacement):
        if part == "engine":
            self.engine = replacement
        elif part == "transmission":
            self.transmission = replacement
        elif part == "drivetrain":
            self.drivetrain = replacement
        else:
            print("Invalid part specified.")
        print(f"The {part} has been replaced with {replacement}.")

    def Reupholster(self, color):
        self.interior_color = color
        print(f"The interior has been reupholstered to {color}.")

    def Drive(self, miles):
        self.mileage += miles
        print(f"The car has been driven {miles} miles. Total mileage is now {self.mileage} miles.")

    def Modify_Price(self, new_price):
        if new_price < 1:
            discount = self.price * new_price
            new_price = self.price - discount
            print(f"The new discounted price is ${new_price:.2f}.")
            confirm = input("Is this the correct desired amount? (yes/no): ")
            if confirm.lower() == "yes":
                self.price = new_price
                print(f"The price has been updated to ${self.price:.2f}.")
            else:
                print("The price has not been changed.")
        else:
            self.price = new_price
            print(f"The price has been updated to ${self.price:.2f}.")

# Example usage
car = Car("Toyota", "Camry", 2020, 15000, "V6", "Automatic", "FWD", 30, "Red", "Black", False, 20000)
car.Paint("Blue")
car.Repair("engine", "V8")
car.Reupholster("Beige")
car.Drive(500)
car.Modify_Price(0.9)


# Define the Seller class
class Seller:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating
        self.inventory = []

    def Buy(self, car):
        if car not in self.inventory:
            self.inventory.append(car)
            print(f"{car.manufacturer} {car.model} has been added to the inventory.")
        else:
            print(f"{car.manufacturer} {car.model} is already in the inventory.")

    def Sell(self, car):
        if car in self.inventory:
            self.inventory.remove(car)
            print(f"{car.manufacturer} {car.model} has been sold.")
        else:
            print(f"{car.manufacturer} {car.model} is not in the inventory.")

# Create a Seller object
seller = Seller("John Doe", 4.5)

# Read the CSV file
df = pd.read_csv("C:/Users/danie/Downloads/cars.csv")  # Replace 'cars.csv' with your CSV file path

# Iterate through the rows of the dataframe and create Car objects
for index, row in df.iterrows():
    car = Car(
        manufacturer=row['manufacturer'],
        model=row['model'],
        year=row['year'],
        mileage=row['mileage'],
        engine=row['engine'],
        transmission=row['transmission'],
        drivetrain=row['drivetrain'],
        mpg=row['mpg'],
        exterior_color=row['exterior_color'],
        interior_color=row['interior_color'],
        accidents_or_damage=row['accidents_or_damage'],
        price=row['price']
    )
    # Add the Car object to the Seller's inventory
    seller.Buy(car)

# Example usage
seller = Seller("John Doe", 4.5)
car1 = Car("Toyota", "Camry", 2020, 15000, "V6", "Automatic", "FWD", 30, "Red", "Black", False, 20000)
car2 = Car("Honda", "Civic", 2019, 20000, "I4", "Manual", "FWD", 35, "Blue", "Gray", False, 18000)

seller.Buy(car1)  # Output: Toyota Camry has been added to the inventory.
seller.Buy(car2)  # Output: Honda Civic has been added to the inventory.
seller.Sell(car1)  # Output: Toyota Camry has been sold.


