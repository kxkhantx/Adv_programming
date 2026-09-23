# Assignment 03 — CHANGES

**Name:** Kaung Khant Htoo  **Student ID:** 6705140027

## 1 · What I changed

| # | Code smell in the original | What I changed it to | OOP concept applied | How I checked behaviour was unchanged |
|---|---|---|---|---|
| 1 | Product information was kept in tuples such as `("Laptop", 1200.0, "electronics")`. | Created a `Product` class with `name`, `price`, and `category`, with some basic validation. | Classes / Encapsulation | Ran the program and checked the product details in the receipts. |
| 2 | Orders and items used tuples with indexes for the customer, product, and quantity. | Created `OrderItem` and `Order` classes. An order contains a customer and multiple order items. | Composition | Ran the self-test and checked that all four receipts were still produced. |
| 3 | The original code had separate `if/elif` chains for each customer tier's discount and points. | Created `Customer`, `SilverCustomer`, `GoldCustomer`, and `PlatinumCustomer` classes with their own methods. | Inheritance / Polymorphism | Checked the discount and points rules and ran the self-test. |
| 4 | `calc()` was doing the calculations and printing the receipt at the same time. | Added separate `subtotal()`, `discount()`, `tax()`, `total()`, and `points()` methods, with `receipt()` used for the output. | Separation of calculation and I/O | Compared the output with the original behaviour and got PASS. |
| 5 | Values such as `100`, `10`, and `0.03` were written directly in the code, and the old code used `global TAXRATE`. | Added named constants such as `DISCOUNT_THRESHOLD`, `BULK_QTY_THRESHOLD`, and `BULK_DISCOUNT_RATE`, and did not use the global in the refactored part. | Clean code | Read through the refactored section and ran `python Assignment_03.py`. |

## 2 · Short reflection

The main change I found useful was putting the customer tiers into separate classes. This made the discount and points code easier to understand than having many `if/elif` statements in one function. I also changed the product, item, and order data into objects so the code does not depend on tuple indexes. Another important part was keeping the calculations separate from the receipt output. I had to be careful because even a small change to the calculations or receipt text would make the self-test fail.

---

## 3 · Prompt log (Level 2 — required)

| # | My prompt to the AI | What it suggested (summary) | Accept / reject / edited | How I checked it |
|---|---|---|---|---|
| 1 | *"Can you help me turn the product and order data into simple classes?"* | Suggested `Product`, `OrderItem`, `Customer`, and `Order` classes and how they could relate to each other. | Edited the structure to keep it simple and match the assignment. | Checked that the objects could be created and ran the self-test. |
| 2 | *"How can I replace the customer tier if/elif code with classes?"* | Suggested a base `Customer` class with Silver, Gold, and Platinum subclasses that handle their own discount and points values. | Accepted the idea and adjusted the method names and class structure. | Checked the discount rates and point multipliers against the original rules. |
| 3 | *"How can I separate the calculations from printing the receipt?"* | Suggested putting the calculations in `Order` methods and making a separate `receipt()` method build the receipt text. | Edited the receipt code so the output stayed exactly the same. | Ran `python Assignment_03.py` and got PASS. |
| 4 | *"What should I change to remove magic numbers and the global variable?"* | Suggested using named constants for the tax, thresholds, bulk discount, and points calculation. | Accepted and used simple constant names in the refactored section. | Read through the code and ran the self-test again. |

**Ownership statement.** By submitting, I confirm I understand and can explain every line of code I submitted, and that this prompt log reflects my actual AI use.

---

## 4 · Before-you-submit checklist

- [x] `python Assignment_03.py` prints **PASS**.
- [x] Products, orders, and items are represented with classes.
- [x] Customer tiers use inheritance and polymorphism.
- [x] Calculation methods return values and receipt printing is separate.
- [x] Constructors validate object state.
- [x] Magic numbers are replaced with named constants in the refactored section.
- [x] The change table and reflection are filled in.
- [x] The prompt log is filled in.
