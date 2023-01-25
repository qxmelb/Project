# Box plots of gene expression sorted by sample type
# Arbitrarily Select Gene on line 36 (ENSG00000237973), index [35]

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from sys import argv

try:
    file = open(argv[1])
except IndexError:
    print("Usage: python3 plot.py dataset")
    exit()

list = []

lines = file.readlines()

# Read gene expression values, skip index 0 as this is the gene text
for num in lines[35].strip().split('\t')[1:]:
    list.append(num)

# There wasn't a way to determine parental cell type from the data provided, so I hard coded this
# Sort by sample type

# Sample type: MDM Control
MDMC = []
for i in [0,8,11]:
    MDMC.append(float(list[i]))

# Sample type: MDM Acute
MDMA = []
for i in [7,9,12]:
    MDMA.append(float(list[i]))

# Sample type: MDM Tolerance
MDMT = []
for i in [10,13]:
    MDMT.append(float(list[i]))

# Sample type: iMac Control
MacC = []
for i in [1,4]:
    MacC.append(float(list[i]))

# Sample type: iMac Acute
MacA = []
for i in [2,5]:
    MacA.append(float(list[i]))

# Sample type: iMac Tolerance
MacT = []
for i in [3,6]:
    MacT.append(float(list[i]))

# Side by side box plots, multiple
# Scale starts from 0
fig, ax = plt.subplots()
ax.set_title('Gene Expression by Sample Type')
ax.set_xlabel('Sample Type')
ax.set_ylabel('Gene Expression (cpm)')
ax.set_xticklabels(['MDM Control', 'MDM Acute', 'MDM Tolerance', 'iMac Control', 'iMac Acute', 'iMac Tolerance'])

data = [MDMC, MDMA, MDMT, MacC, MacA, MacT]
ax.boxplot(data)
ax.set_ylim(bottom = 0)
plt.show()
file.close()
