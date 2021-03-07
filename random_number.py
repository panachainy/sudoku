from random import seed
from random import randint
from datetime import date

# seed random number generator
seed(date.today())


def get_random_number(start, end):
    return randint(start, end)

# # test random 10 value
# for _ in range(10):
#     value = get_random_number(0,10)
#     print(value)
