car = "subaru"
food = "pizza"
age = 25
temperature = 72
is_sunny = True

# 5 Tests that evaluate to True

print("Test 1: Is car == 'subaru'? I predict True.")
print(car == "subaru")

print("\nTest 2: Is food == 'pizza'? I predict True.")
print(food == "pizza")

print("\nTest 3: Is age == 25? I predict True.")
print(age == 25)

print("\nTest 4: Is temperature > 60? I predict True.")
print(temperature > 60)

print("\nTest 5: Is is_sunny == True? I predict True.")
print(is_sunny == True)


# 5 Tests that evaluate to False

print("\nTest 6: Is car == 'audi'? I predict False.")
print(car == "audi")

print("\nTest 7: Is food == 'burger'? I predict False.")
print(food == "burger")

print("\nTest 8: Is age < 18? I predict False.")
print(age < 18)

print("\nTest 9: Is temperature == 100? I predict False.")
print(temperature == 100)

print("\nTest 10: Is is_sunny == False? I predict False.")
print(is_sunny == False)

# Variables for testing
car = "Audi"
food = "pizza"
age = 21
price = 50
requested_toppings = ["mushrooms", "onions", "pineapple"]

# Tests for equality and inequality with strings
print("Is car == 'Audi'? I predict True.")
print(car == "Audi")

print("\nIs car == 'subaru'? I predict False.")
print(car == "subaru")

# Tests using the lower() method
print("\nIs car.lower() == 'audi'? I predict True.")
print(car.lower() == "audi")

print("\nIs car.lower() == 'Audi'? I predict False.")
print(car.lower() == "Audi")

# Numerical tests involving equality, inequality, >, <, >=, <=
print("\nIs age == 21? I predict True.")
print(age == 21)

print("\nIs age != 21? I predict False.")
print(age != 21)

print("\nIs age > 18? I predict True.")
print(age > 18)

print("\nIs age < 18? I predict False.")
print(age < 18)

print("\nIs price >= 50? I predict True.")
print(price >= 50)

print("\nIs price <= 40? I predict False.")
print(price <= 40)

# Tests using the 'and' keyword and the 'or' keyword
print("\nIs age > 18 and price >= 50? I predict True.")
print(age > 18 and price >= 50)

print("\nIs age > 18 and price > 100? I predict False.")
print(age > 18 and price > 100)

print("\nIs age > 25 or price == 50? I predict True.")
print(age > 25 or price == 50)

print("\nIs age > 25 or price < 20? I predict False.")
print(age > 25 or price < 20)

# Test whether an item is in a list
print("\nIs 'mushrooms' in requested_toppings? I predict True.")
print("mushrooms" in requested_toppings)

print("\nIs 'pepperoni' in requested_toppings? I predict False.")
print("pepperoni" in requested_toppings)

# Test whether an item is not in a list
print("\nIs 'pepperoni' not in requested_toppings? I predict True.")
print("pepperoni" not in requested_toppings)

print("\nIs 'mushrooms' not in requested_toppings? I predict False.")
print("mushrooms" not in requested_toppings)