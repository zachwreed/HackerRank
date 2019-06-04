import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range(n):
        j = n - i - 1
        for k in range(j):
            print(' ', end="")
        
        for l in range(i + 1):
            if l == i:
                print ("#")
            else:
                print("#", end="")



if __name__ == '__main__':
    n = int(input())

    staircase(n)
