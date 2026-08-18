def send_invites(guests: list):
    for name in guests:
        print(f"Good day Mr. {name}, you are invited to annivesary dinner")
    print("\n")

def seperating_block(msg: str):
    print("="*40)
    print(f"{msg}")
    print("="*40)

guest_list = ["Jona","Joseph","Samuel","Jenkins"]
send_invites(guest_list)

print(f"So Mr. {guest_list[-1]} cannot make it")

guest_list[-1] = "Ransom"
send_invites(guest_list)

print("I found a bigger dinning hall!\n")

guest_list.insert(0, "Frank")
guest_list.insert((len(guest_list) // 2), "Gerald")
guest_list.append("Raynold")
send_invites(guest_list)

print("The Dinning hall could not be resolved in time, sorry for the inconvenince, I can only invite 2 persons.\n")

range_end = len(guest_list) - 2
for _ in range(range_end):
    removed_guest = guest_list.pop()
    print(f"Sorry Mr. {removed_guest} you have been uninvited")

print("\n")
send_invites(guest_list)
print(guest_list)

for i in range(len(guest_list) -1, -1, -1):
    del guest_list[i]
print("WE should have no guests", guest_list)

seperating_block("Section 3 exercises")

places = ['Tokyo', 'Enugu', 'Jersey', 'Santorini', 'Kyoto']
print('Original list: ', places, "\n")

print('Sorted list:', sorted(places))
print('Original list: ', places, "\n")


print('Sorted in reverse: ',sorted(places, reverse=True))
print('Original list: ', places, "\n")


places.reverse()
print('List reversed: ', places, "\n")


places.reverse()
print('Original list: ', places, "\n")


places.sort()
print('List sorted inplace: ', places, "\n")


places.sort(reverse=True)
print('List sorted inplace reverse: ', places, "\n")

guest_list = ["Jona","Joseph","Samuel","Jenkins"]
print("Number of guests: ", len(guest_list))

languages = ['Python', 'Rust', 'JavaScript', 'Go']

print("List of interests",languages)

print(len(languages))

languages.append('Solidity')
print(languages)

languages.insert(0, 'C++')
print(languages)

languages.remove('Rust')
print(languages)

popped = languages.pop()
print(popped)
print(languages)

first_choice = languages.pop(0)
print(first_choice)
print(languages)

del languages[1]
print(languages)

languages.sort()
print(languages)

languages.sort(reverse=True)
print(languages)

print(sorted(languages))
print(languages)

languages.reverse()
print(languages)

print(len(languages))


seperating_block("Section 4 exercises")

# Print 1 to 20
# for i in range(21):
#     print(i)

list_of_one_million = [i for i in range(1, 1_000_001)]
# Print form 1 to 1 million
# for num in list_of_one_million:
#     print(num)

print(f"Min of list: {min(list_of_one_million)}\nMax of list: {max(list_of_one_million)}")

print("Sum of list: ", sum(list_of_one_million))

odd_nums = [i for i in range(1,21,2)]
# Print odd numbers
# for num in odd_nums:
#     print(num)

multiples_of_3 = [i for i in range(3,31,3)]
# Print the multiples of 3
# for num in multiples_of_3:
#     print(num)

cube_of_nums = [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
# for i in cube_of_nums:
#    print(i)

cube_of_nums = [i**3 for i in range(1, 11)]

seperating_block("Section 4 part 2 exercises")
print("Reference list: ",places)
print(f"First three items: {places[:3]}")
mid_list = len(places) // 2

print("Three items from the middle of the list are: ",places[mid_list-1:mid_list+2])
print('The last three items in the list are: ', places[-3:])

friends_pizza = ["Silican",'Roman','Neopolitan']
for pizza in friends_pizza:
    print(f"Cena loves {pizza} pizza")

pizzas = ['pepperoni', 'margherita', 'bbq chicken']
for pizza in pizzas:
    print(f"I really like {pizza} pizza.")
print("I love pizza so very much!")

animals = ['Lion', 'Tiger', 'Leopard', 'Cougar', 'Jaguar']
for animal in animals:
    print(animal)

for animal in animals:
    print(f"A {animal} looks very scary")
print("These are all wildcats!")

menu = ('shrimps', 'Pasta', 'Pizza', 'Garri', 'Naan')
for item in menu:
    print(item)
# menu[0] = 'Suya'  # throws a TypeError

new_menu = ('shrimps', 'Soup', 'Pizza', 'Suya', 'Naan')
for item in menu:
    print(item)