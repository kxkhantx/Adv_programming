# Siam University Vehicle Rental System

## How I used AI

I used AI to help me understand the assignment requirements and explain Python OOP concepts.

## OOP Concepts Included:

- **Classes and Objects:**  
  Created classes such as `Vehicle`, `Renter`, `ElectricCar`, and `Motorbike` to represent vehicles and renters.

- **Encapsulation:**  
  Used properties and setters for `name` and `license_no` in the `Renter` class. The setters also validate the input and raise an error when the value is invalid.

- **Inheritance:**  
  `ElectricCar` and `Motorbike` inherit from the `Vehicle` class and reuse its attributes and methods.

- **Polymorphism:**  
  `ElectricCar` and `Motorbike` override the `__str__()` method from the `Vehicle` class to display their own additional information, such as battery capacity and engine size.

## Project Structure

- `rental.py`
- `main.py`

## Project Execution

Run this in your terminal:

```bash
python main.py
```
