import numpy as np
import contextlib
import math
np.set_printoptions(threshold=np.nan)


@contextlib.contextmanager
def printoptions(*args, **kwargs):
    original = np.get_printoptions()
    np.set_printoptions(*args, **kwargs)
    try:
        yield
    finally:
        np.set_printoptions(**original)

file = open("./sample.txt")
#281905
array = [[0 for i in range(12)] for j in range(12)]

for line in file:
    i=i+1
    content = line.strip().split()
    nb = int(content[0])-1
    ne = int(content[1])-1
    array[nb][ne]=1

file.close()

a=np.array(array)
u,s,v = np.linalg.svd(a, full_matrices=False,compute_uv=1)

with printoptions(precision=2, suppress=True):
    print(s)
print
print



with printoptions(precision=2, suppress=True):
    print(u)



print("done")



