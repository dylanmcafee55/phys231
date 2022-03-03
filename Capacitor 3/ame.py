import os
import numpy as np
path = os.getcwd()


f = []
for (dir, sub, files) in os.walk(path):
    for file in files:
        f.append(file)
f.sort()
print(f)
for i in range
