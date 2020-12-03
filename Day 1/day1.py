import pandas as pd
import math
import numpy as np

with open('data.txt') as f:
    lines = [int(line.rstrip()) for line in f]

sol = []
for x in lines:
    for y in lines:
        for z in lines:
            if x + y + z == 2020:
                sol.append(x)
                sol.append(y)
                sol.append(z)
            if sol:
                break
print(sol)
print(np.prod(sol))

