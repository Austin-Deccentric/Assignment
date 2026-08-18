pizza_toppings = input("Enter a pizza topping: ")
while pizza_toppings != 'quit':
    print(f"Adding {pizza_toppings} to your pizza")
    pizza_toppings = input("Enter a pizza topping: ")

age = int(input("Enter your age: "))
while age != 0:
    if age < 3:
        print('The ticket is free')
    elif age < 13:
        print('The ticket is $10')
    else:
        print('The ticket is $15')
    age = int(input("Enter your age: "))


# excersie 7-6
pizza_toppings = input("Enter a pizza topping: ")
num = 0
while num < 7:
    print(f"Adding {pizza_toppings} to your pizza")
    pizza_toppings = input("Enter a pizza topping: ")
    if pizza_toppings == 'pineapple':
        print('Sorry, we are not serving pineapple')
        break
    if pizza_toppings == 'quit':
        break
    num += 1

# while True:
#     print('Infiinity')

# 7-9
sandwich_orders: list[str] = ['burger', 'tuna', 'chicken', 'pastrami', 'mackrel', 'pastrami', 'sardine', 'pastrami']
print("We are out of pastrami")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# excersie 7-8
# sandwich_orders: list[str] = ['burger', 'tuna', 'chicken', 'mackrel', 'sardine']
finished_sandwich: list[str] = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"Making sandwich with {sandwich} ")
    finished_sandwich.append(sandwich)
print(f"Finished making {', '.join(finished_sandwich)} sandwiches")

# execerise 7-10
responses = {}

polling_active = True

while polling_active:
    name = input("\nEnter your username? ")
    response = input("If you could visit one place in the world, where would you go? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == "no":
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to visit {response}.")


