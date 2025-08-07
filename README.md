This application performs several operations related to car management and inventory tracking.

### 1. Car Class
The Car class represents a car with various attributes and methods for managing the car's state. The attributes include manufacturer, model, year, mileage, engine type, transmission type, drivetrain, miles per gallon (mpg), exterior and interior colors, accident history, and price.

**Methods:**
- Paint(color): Changes the car's exterior color and prints a confirmation message.
- Repair(part, replacement): Replaces a specified part (engine, transmission, or drivetrain) and prints a confirmation message.
- Reupholster(color): Changes the car's interior color and prints a confirmation message.
- Drive(miles): Increases the car's mileage by a specified number of miles and prints the new mileage.
- Modify_Price(new_price`: Updates the car's price. If the new price is less than 1, it applies a discount based on the original price and asks for confirmation before updating. Otherwise, it directly sets the new price.

### 2. Seller Class
The Seller class represents a car seller with a name, a rating, and an inventory of cars.

**Methods:**
- Buy(car): Adds a car to the seller's inventory if it's not already present and prints a confirmation message.
- Sell(car): Removes a car from the seller's inventory if it's present and prints a confirmation message.

### 3. CSV File Processing
- Reads car data from a CSV file located at `"C:/Users/danie/Downloads/cars.csv"`.
- Iterates through each row of the dataframe created from the CSV file and creates Car objects using the data from each row.
- Adds each created Car object to the Seller’s inventory using the Buy method.

### 4. Example Usage
- A Seller object is created with the name "John Doe" and a rating of 4.5.
- Two Car objects are instantiated (car1 and car2) and added to the seller's inventory.
- The Buy method is used to add the cars to the inventory, and the Sell method is used to remove one car from the inventory.
