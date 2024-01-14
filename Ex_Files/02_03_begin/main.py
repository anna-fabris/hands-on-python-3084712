# This code is about LISTS:
NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

JOHN = NAMES[0]
PAUL = NAMES[1]

# the slice [:] can be used also for strings
JOHN_PAUL = NAMES[:2]
GEORGE_RINGO = NAMES[2:]
REVERSE = NAMES[::-1] 
# reverse: start - stop - step
EVERY_OTHER = NAMES[::2]
# every other: just the step

print(sum(AGES))
print(min(AGES))
print(max(AGES))

print(JOHN_PAUL)
print(GEORGE_RINGO)
print(REVERSE)
