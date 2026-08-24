# 10-6
x = input("Enter a number: ")
y = input("Enter another number: ")
try:
    x = int(x)
    y = int(y)
    result = x + y
    print(result)
except ValueError:
    print("Invalid input, please enter a number")

# 10-7
while True:
    first = input("First number: ")
    if first.lower() == 'q':
        break
    
    second = input("Second number: ")
    if second.lower() == 'q':
        break
    
    try:
        result = int(first) + int(second)
    except ValueError:
        print("You must enter numbers, not text. Try again.\n")
    else:
        print(f"The sum is: {result}\n")


# 10-8
def read_pet_file(filename):
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file '{filename}' was not found.")
    else:
        print(f"Contents of {filename}:")
        print(contents)

read_pet_file('cats.txt')
read_pet_file('dogs.txt')

# 10-9
def read_pet_file_silent(filename):
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        print(f"Contents of {filename}:")
        print(contents)

read_pet_file_silent('cats.txt')
read_pet_file_silent('dogs.txt')
