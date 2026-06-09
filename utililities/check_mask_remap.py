import numpy as np

mask = np.array([0, 1, 2, 4])

mask[mask == 4] = 3

print(np.unique(mask))