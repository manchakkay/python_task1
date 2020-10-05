import matplotlib.pyplot as plt
import numpy as np


input = open("figure6.txt")
lines = input.readlines()

real_size = float(lines[0])
min_i = 1000000000
max_i = -1


for i, line in enumerate(lines):
    arr = np.array(line.strip().split(" "))

    for j, elem in enumerate(arr):
        if elem.isdigit() and (int(elem) == 1) and (i > 1):
            if min_i > i:
                min_i = i
            if max_i < i:
                max_i = i


print(real_size / (max_i - min_i + 1))