# 9-1
class Restaurant:
    def __init__(self, restuarant_name: str, cuisine_type: str):
        self.restaurant_name: str = restuarant_name
        self.cuisine_type: str = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant: {self.restaurant_name}")
        print(f"Cuisine: {self.cuisine_type}")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")

restaurant = Restaurant("Pizza Palace", "Italian")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

#9-2
restaurant2 = Restaurant("Sushi Spot", "Japanese")
restaurant2.describe_restaurant()

restaurant3 = Restaurant("", "")
restaurant3.describe_restaurant()

# 9-3
class User:
    def __init__(self, first_name: str, last_name: str, age: int):
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.age: int = age

    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")

    def greet_user(self):
        print(f"Hello, {self.first_name}!")

user = User("John", "Range", 30)
user.describe_user()
user.greet_user()

user2 = User("Mary", "Blood", 27)
user2.describe_user()
user2.greet_user()

user3 = User("Jorge", "Mendez", 90)
user3.describe_user()
user3.greet_user()

# 9-4
class Restaurant:
    def __init__(self, restuarant_name: str, cuisine_type: str):
        self.restaurant_name: str = restuarant_name
        self.cuisine_type: str = cuisine_type
        self.number_served: int = 0

    def describe_restaurant(self):
        print(f"Restaurant: {self.restaurant_name}")
        print(f"Cuisine: {self.cuisine_type}")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")

    def set_number_served(self, number_served: int):
        self.number_served = number_served

    def increment_number_served(self, number: int):
        self.number_served += number

restaurant = Restaurant("Pizza Palace", "Italian")
print(restaurant.number_served)

restaurant.set_number_served(10)
print(restaurant.number_served)

restaurant.increment_number_served(5)
print(restaurant.number_served)

# 9-5
class User:
    def __init__(self, first_name: str, last_name: str, age: int):
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.age: int = age
        self.login_attempts: int = 0

    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")

    def greet_user(self):
        print(f"Hello, {self.first_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


# 9-6
class IceCreamStand(Restaurant):
    def __init__(self, restuarant_name: str, cuisine_type: str):
        super().__init__(restuarant_name, cuisine_type)
        self.flavors: list[str] = ["Milkshake Shack", "Ice Cream"]

    # def add_flavor(self, flavor: str):
    #     self.flavors.append(flavor)

    def display_flavors(self):
        print("Flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")

ice_cream_stand = IceCreamStand("Mikky's Creamry", "Ice cream")
ice_cream_stand.display_flavors()

# 9-7
class Admin(User):
    def __init__(self, first_name: str, last_name: str, age: int):
        super().__init__(first_name, last_name, age)
        self.privileges: list[str] = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

admin = Admin("Matty", "Oluwa", 30)
admin.show_privileges()

# 9-8
class Privileges:
    def __init__(self):
        self.privileges: list[str] =  ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


# privilege = Privileges(["can add post", "can delete post", "can ban user"])


class Admin(User):
    def __init__(self, first_name: str, last_name: str, age: int):
        super().__init__(first_name, last_name, age)
        self.privileges: Privileges = Privileges()

admin = Admin("Matty", "Oluwa", 30)
admin.privileges.show_privileges()
