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


class Admin(User):
    def __init__(self, first_name: str, last_name: str, age: int):
        super().__init__(first_name, last_name, age)
        self.privileges: Privileges = Privileges()

class Privileges:
    def __init__(self):
        self.privileges: list[str] =  ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")