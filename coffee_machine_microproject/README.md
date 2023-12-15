# Microproject - Coffee Machine

The Coffee Maker System is a Python-based program that simulates a coffee machine. It includes several classes to model different aspects of the coffee-making process. The system comprises the following files:

## 1. coffee_maker.py

This file defines the `CoffeeMaker` class, representing the coffee-making machine. It includes the following methods:

- `__init__(self)`: Initializes the resources available in the coffee maker.
- `report(self)`: Prints a report of all available resources.
- `is_resource_sufficient(self, drink)`: Checks if there are enough resources to make a specific drink.
- `make_coffee(self, order)`: Deducts the required ingredients from the resources to make a coffee.

## 2. main.py

The `main.py` file serves as the entry point for the coffee maker system. It includes the main loop to interact with the user, providing options to order coffee, view reports, and turn off the machine.

## 3. menu.py

This file contains two classes:

- `MenuItem`: Models each menu item with a name, cost, and ingredients.
- `Menu`: Models the overall menu with a list of available drinks and methods to retrieve items and find a specific drink.

## 4. money_machine.py

The `MoneyMachine` class in this file models the money-handling component of the system. It includes methods to process coins, make payments, and report the current profit.

The system employs an object-oriented approach, separating concerns into different classes, enhancing modularity, and facilitating future expansions or modifications.
