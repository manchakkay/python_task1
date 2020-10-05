import matplotlib.pyplot as plt
import numpy as np

input1 = open("img1.txt")
input2 = open("img2.txt")

fir_i = 1000000000
sec_i = 1000000000
fir_j = 1000000000
sec_j = 1000000000

lines = input1.readlines()
for i, line in enumerate(lines):
    arr = np.array(line.strip().split(" "))

    for j, elem in enumerate(arr):
        if elem.isdigit() and (int(elem) == 1) and (i > 1):
            if fir_i > i:
                fir_i = i
            if fir_j > j:
                fir_j = j

lines = input2.readlines()
for i, line in enumerate(lines):
    arr = np.array(line.strip().split(" "))

    for j, elem in enumerate(arr):
        if elem.isdigit() and (int(elem) == 1) and (i > 1):
            if sec_i > i:
                sec_i = i
            if sec_j > j:
                sec_j = j

print("X:", sec_j - fir_j,"|| Y:", sec_i - fir_i,  sep=' ')
