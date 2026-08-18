
unames = ['admin', 'swagger', 'hero', 'fred', 'henny']
for user in unames:
    if user == 'admin':
        print(f"Hello {user}, would you like to see a status report?")
    print(f"Hello {user} thank you for logging in again")

for _ in range(len(unames)):
    _ = unames.pop()

if not unames:
    print("We need to find some users!")

current_users = ['Homer', 'swagger', 'hero', 'fred', 'henny']
current_users_lower = [user.lower() for user in current_users]
new_users = ['Uvie', 'Calyso', 'Henny', 'Hector', 'Agamenon']
for user in new_users:
    if user.lower() in current_users_lower:
        print(f"{user} is taken, please choose another username")
    else:
        print(f"{user} is available")

num_list = [i for i in range(1,10)]
for i in num_list:
    if i == 1:
        print(f"{i}st")
    elif i == 2:
        print(f"{i}nd")
    elif i == 3:
        print(f"{i}rd")
    else:
        print(f"{i}th")
