print("=" * 50)
print("Question 1: Student Grade List")
print("=" * 50)

grades = [85, 92, 78,95, 88]
grades.append(90)
grades.sort()
print("Sorted Grades:", grades)
print("Highest Grade:", grades[-1])
print("Lowest Grade:", grades[0])
print("Total Number of Grades:", len(grades))
print()

print("=" * 50)
print("Question 2: Shopping Cart")
print("=" * 50)
cart = ["apple", "banana", "milk", "bread", "apple", "eggs"]
apple_count = cart.count("apple")
print("Number of apples:", apple_count)
milk_position = cart.index("milk")
print("Position of milk:", milk_position)
cart.remove("apple")
remove_item = cart.pop()
print("Removed item using pop:", remove_item)
print("Is banana in the cart?", "banana" in cart)
print("Final cart:", cart)
print()

print("=" * 50)
print("Question 3: Inventory Management")
print("=" * 50)
point1 = (3,5)
print("Point 1:", point1)
point2 = (7,2)
print("Point 2:", point2)
x1, y1 = point1
print("x1 =", x1, "y1 =", y1)
x2, y2 = point2
print("x2 =", x2, "y2 =", y2)
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print("Distance between points", distance)
char_tuple = tuple("PYTHON")
print("Character Tuple:", char_tuple)
for char in char_tuple:
    print(char)
print()

print("=" * 50)
print("Question 4: Class Attendance")
print("=" * 50)
monday_class = {"Alice", "Bob", "Charlie", "Diana"}
wednesday_class = {"Bob", "Diana", "Eve", "Frank"}
monday_class.add("Grace")
print("Monday Class:", monday_class)
print("Wednesday Class:", wednesday_class)
both_classes = monday_class & wednesday_class
print("Students in both classes:", both_classes)
all_students = monday_class | wednesday_class
print("Atended either classes:", all_students)
only_monday = monday_class - wednesday_class
print("Only Monday:", only_monday)
only_one = monday_class ^ wednesday_class
print("Only one class:", only_one)
print("Is Monday subset all students?", monday_class <= all_students)
print()

print("=" * 50)
print("Question 5: Contact Book")
print("=" * 50)
contacts = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9999"
}
print("Alice's number:", contacts["Alice"])
contacts["Diana"] = "555-4321"
print("Contacts after adding Diana:", contacts)
contacts["Bob"] = "555-0000"
print("Contacts after updating Bob's number:", contacts)
del contacts["Charlie"]
print("Contacts after deleting Charlie:", contacts)
print("All names:", contacts.keys())
print("All numbers:", contacts.values())
print("Total contacts:", len(contacts))
print()

print("=" * 50)
print("Question 6: Inventory Management System")
inventory = {
    "Laptop": (999.99, 5),
    "Mouse": (29.99, 15),
    "Keyboard": (79.99, 10),
    "Monitor": (299.99, 8)
}
print("=== Current Inventory ===")
for product, details in inventory.items():
    price = details[0]
    quantity = details[1]
    print(product + " - Price: $" + str(price) + ", Quantity: " + str(quantity))
print() 
electronics ={"Laptop", "Monitor"}
accessories ={"Mouse", "Keyboard"}
prices = [] 
for product in inventory:
    price = inventory[product][0]
    prices.append(price)
print("Price list:", prices)
prices.sort() 
print("Sorted prices:", prices)
print("Lowest price: $", prices[0])
print("Highest price: $", prices[-1])
print()
inventory["Headphones"] = (49.99, 20)
mouse_price = inventory["Mouse"][0]
inventory["Mouse"] = (mouse_price, 12)
del inventory["Monitor"]
print("=== Final Inventory ===")
for product, details in inventory.items():
    price = details[0]
    quantity = details[1]
    print(product + " - Price: $" + str(price) + ", Quantity: " + str(quantity))