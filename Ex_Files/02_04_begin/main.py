# Loops in python are mainly of 2 types: 
# 1) While loops
# 2) For...in (more popular, less bug prone and more readable)

NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

i = 0
while i < len(NAMES):
    print(NAMES[i], AGES[i])
    i += 1

for name in NAMES:
    print(name)

for name, age in zip(NAMES, AGES):
    print(f"{name} {age}")

for name in reversed(NAMES):
    print(name)

for i in range(5):
    print(i)

# enumerate (to keep track of the iter number)
for i, name in enumerate(NAMES):
    print(f"{i} {name}")