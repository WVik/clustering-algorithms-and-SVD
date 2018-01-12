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

file = open("./dataset.txt")
#281905
array = [[0 for i in range(1007)] for j in range(1007)]
i=0
for line in file:
    i=i+1
    content = line.strip().split()
    nb = int(content[0])-1
    ne = int(content[1])-1
    if(i==1000):
        print("here")
    array[nb][ne]=1

file.close()

file = open("./singulars.txt",'w')

a=np.array(array)
u,s,v = np.linalg.svd(a, full_matrices=False,compute_uv=1)

with printoptions(precision=2, suppress=True):
    print(s)
print
print
count=0
##for i in s:
  ##  if(i>1.5):
    ##    count=count+1


arr = u[:,0]
#arr=arr.sort()
#print(arr)

for i in arr:
    if(i>0.001):
        count=count+1


print(count)
print("done")



