from itertools import *
from math import *
f = open(r"wordlist.txt", "a+")
s = 0
for i in permutations('1234567890abcdefghijklmnopqrstuvwxyz',8):
    i = list(i)
    i = str(i)
    f.write(i)
    print(i)
    #print(i)
