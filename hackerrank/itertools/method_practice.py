import itertools
from itertools import *
#itertools return itrable object
def count_1(l): # Generates an infinite iterator that returns consecutive integers starting from the start with a step of step.
    l  = l
    for i in zip(count(1,1),l):
        print(i)

def cycle_1(l):
    c = cycle(l)
    for i in range(10):
        print(next(c))

l = ["a","b","c","d"]

# c = count_1(l)
c = cycle_1(l)