import numpy as np

def heads_in_a_row(flips, p, want):
    a = np.zeros((want + 1, want + 1))
    for i in range(want):
        a[i, 0] = 1 - p
        a[i, i + 1] = p
    a[want, want] = 1.0
    return np.linalg.matrix_power(a, flips)[0, want]

print(heads_in_a_row(flips=100, p=0.04, want=2))