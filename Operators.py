import math
import os
import random
import re
import sys

def solve(meal_cost, tip_percent, tax_percent):
    my_tip = meal_cost * tip_percent/100
    my_tax = meal_cost * tax_percent/100
    my_total_cost = meal_cost + my_tip + my_tax
    
    print(str(round(my_total_cost)))

if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
