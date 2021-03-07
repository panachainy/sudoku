from random import seed
from random import randint

# seed random number generator
seed(1)


def get_random_number(start, end):
    return randint(start, end)

# # test random 10 value
# for _ in range(10):
#     value = get_random_number(0,10)
#     print(value)
