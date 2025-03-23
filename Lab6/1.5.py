from functools import reduce
from operator import mul
import time
import math
def true(iterable_elements):
    return all(iterable_elements)

print(true((True, True, True)))
print(true((False, False, True)))
print(true((False, False,True, True, False)))
