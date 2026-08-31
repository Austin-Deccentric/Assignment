from random import randint, sample, choice
import string


class Die:
    def __init__(self, sides: int = 6):
        self.sides: int = sides

    def roll_die(self):
        # print(f"Die of {self.sides} sides rolled: {randint(1, self.sides)}")
        return randint(1, self.sides)

d_6 = Die()
d_10 = Die(10)
d_20 = Die(20)
results = []

for i in range(10):
    results.append(d_6.roll_die())

print(f"Results for six-sided die: {', '.join(map(str, results))}")
results.clear()

for i in range(10):
    results.append(d_10.roll_die())
    
print(f"Results for ten-sided die: {', '.join(map(str, results))}")
results.clear()


for i in range(10):
    results.append(d_20.roll_die())

print(f"Results for twenty-sided die: {', '.join(map(str, results))}")
results.clear()

numbers = sample(range(1, 20), 10)
letters = sample(string.ascii_lowercase, 5)
alpha_numeric = [*numbers, *letters]
lottery_pick = sample(alpha_numeric, 4)
print(lottery_pick)

num_iterations = 0
won = False

while not won:
    my_ticket = sample(alpha_numeric, 4)
    num_iterations += 1

    if lottery_pick == my_ticket:
        won = True

print(f"Number of iterations: {num_iterations}")
print(f"My ticket: {my_ticket}")
