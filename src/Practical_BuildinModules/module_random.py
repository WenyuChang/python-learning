__author__ = 'wenychan'

import random

for i in range(5):
    # random float: 0.0 <= number < 1.0
    print random.random(),
    # random float: 10 <= number < 20
    print random.uniform(10, 20),
    # random integer: 100 <= number <= 1000
    # Note that randint function can return the upper limit,
    # while the other functions always returns values smaller than the upper limit.
    print random.randint(100, 1000),
    # random integer: even numbers in 100 <= number < 1000
    print random.randrange(100, 1000, 2)


# random choice from a list
for i in range(5):
    print random.choice([1, 2, 3, 5, 9])


numbers = range(10)
random.shuffle(numbers)
print numbers