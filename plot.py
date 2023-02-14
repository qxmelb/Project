import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from sys import argv

try:
    file = open(argv[1])
except IndexError:
    print("Usage: python3 plot.py dataset")
    exit()

# Array of entry lines, prepare data for input into matplotlib
array = file.readlines()
data = []

# Arbitrarily Select Gene on line 36 (ENSG00000237973)
# Account for tab spacing and remove gene identifier on col 1
for num in array[35].strip().split('\t')[1:]:
    data.append(float(num))

# Enter data into boxplot
plot = plt.boxplot(data)
plt.show()
file.close()


