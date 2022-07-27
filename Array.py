import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    array = list(map(int, input().rstrip().split()))

    print(*array[::-1])