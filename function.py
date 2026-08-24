
# def make_shirt(size: str, msg: str):
#     print(f"You want a shirt of size {size} with this: '{msg}' printed on it")
# make_shirt("XL", "Championes")

# def make_shirt(size: str = "large", msg:str = "I love Python"):
#     print(f"You want a shirt of size {size} with this: '{msg}' printed on it")

# make_shirt()
# make_shirt(size="medium")
# make_shirt(size="small", msg="I Love GO")

# def describe_city(city: str, country: str = "Nigeria"):
#     print(f"{city} is in {country}")

# describe_city("Enugu")
# describe_city("Owerri")
# describe_city("Kyoto", 'Japan')

# def city_country(city: str, country: str):
#     return f"{city}, {country}"

# print(city_country("Enugu", "Nigeria"))
# print(city_country("Owerri", "Nigeria"))
# print(city_country("Kyoto", 'Japan'))

# def make_album(artist_name: str, album_title: str, num_of_songs: int |None = None) :
#     album = {}
#     album['artist'] = artist_name
#     album['title'] = album_title
#     if num_of_songs:
#         album['num_of_songs'] = num_of_songs
#     return album

# print(make_album("Queen", "Bohemian Rhapsody"))
# print(make_album("2face", "African Queen"))
# print(make_album("St. Jhn", "Crosses"))
# print(make_album("Queen", "Bohemian Rhapsody", 10))

# artist_name = input("Enter artist name: ")
# while artist_name != "quit":
#     album_title = input("Enter album title: ")
#     print(make_album(artist_name, album_title))
#     artist_name = input("Enter artist name: ")

msg_list = ['Can we be friends', 'Why are you being mean', "Let's make today count"]

def show_messages(messages: list[str]):
    sent_messages: list[str] = []
    for msg in messages:
        print(msg)
        sent_messages.append(msg)
    return sent_messages

sent_messages: list[str] = show_messages(msg_list[:]) # Prints the messages and saves the sent messages
print("-------------Sent Messages---------------")
print(sent_messages)

# sandwich_fillings = ['bacon', 'cheese', 'hotdog', 'salad']
def sandwich_order(*fillings: str):
    print(f"We have an order with this filling(s): {', '.join(fillings)}")

sandwich_order('bacon', 'hotdog', 'salad')
sandwich_order('hotdog', 'salad')
sandwich_order('salad')

def build_profile(first: str, last: str, **user_info: str):
    """Build a dictionary containing everything we know about
    a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('Austin', 'Chukwu',
location='Enugu',
field='CSC')
# print(user_profile)

def make_car(manufacturer: str, model: str, **car_info: str | int):
    """Build a dictionary containing everything we know about
    a car."""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

car = make_car('Toyota', 'Camry',
color='blue',
year=2020)
print(car)
