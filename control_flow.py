alien_color = 'green'
if alien_color == 'green':
    print("You just earned +5 points")
if alien_color != 'green':
    print('')

alien_color = 'red'
if alien_color == 'green':
    print("You just earned +5 points")
else:
    print("You just earned +10 points")

if alien_color == 'red':
    print("You just earned +5 points")
else:
    print("You just earned +10 points")

if alien_color == 'green':
    print("You just earned +5 points")
elif alien_color == 'yellow':
    print("You just earned +10 points")
elif alien_color == 'red':
    print('You just earned +15 points')

alien_color = 'green'

if alien_color == 'green':
    print("You just earned +5 points")
elif alien_color == 'yellow':
    print("You just earned +10 points")
elif alien_color == 'red':
    print('You just earned +15 points')

alien_color = 'yellow'
if alien_color == 'green':
    print("You just earned +5 points")
elif alien_color == 'yellow':
    print("You just earned +10 points")
elif alien_color == 'red':
    print('You just earned +15 points')



age = 25
if age < 2:
    print("The person is a baby.")
elif age < 4:
    print("The person is a toddler.")
elif age < 13:
    print("The person is a kid.")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")

def seperating_block(msg: str):
    print("="*40)
    print(f"{msg}")
    print("="*40)

