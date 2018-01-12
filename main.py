import numpy as np
import contextlib
import math

@contextlib.contextmanager
def printoptions(*args, **kwargs):
    original = np.get_printoptions()
    np.set_printoptions(*args, **kwargs)
    try:
        yield
    finally:
        np.set_printoptions(**original)

size = 10
c = 6

a = np.random.randint(5, size=(size,size))
print(a)

mA = np.asmatrix(a)

print("\n")

print("The matrices U, s, and V are as follows: \n")

U, s, V = np.linalg.svd(a, full_matrices=False)

with printoptions(precision=2, suppress=True):
    print(U)

print("\n")

with printoptions(precision=2, suppress=True):
    print(np.diag(s))

print("\n")

with printoptions(precision=2, suppress=True):
    print(V)

deleteIndex = []


for i in range(0,size):
    if(s[i]<2):
        deleteIndex.append(i)

nS = s
nU = U

for i in deleteIndex:
    nS = np.delete(s,i)
    nU = np.delete(U,i,1)
    nV = np.delete(V,i,0)



print("\n\nThe new matrices are: \n\n")

with printoptions(precision=2, suppress=True):
    print(nU)

print("\n")

with printoptions(precision=2, suppress=True):
    print(np.diag(nS))

print("\n")

with printoptions(precision=2, suppress=True):
    print(nV)

mS = np.asmatrix(np.diag(nS))
mU = np.asmatrix(nU)
mV = np.asmatrix(nV)


print("\n \n \n")


# The approximation to the original matrix is given by:
with printoptions(precision=3, suppress=True):
    print(mU*mS*mV)

print("\n")
print("\n")


# Code for finding probabilities to compute SVD
mATrans = np.matrix.transpose(mA)
frobeniusNorm = np.linalg.norm(a)   #Inbuilt function to compte Frobenius norm
probabilites = []                   #Array for storing probabilities of each column

for i in range(0,size):
    colNorm = np.linalg.norm(mATrans[i], 2) #Column Norm for each column
    probabilites.append((colNorm**2)/(frobeniusNorm**2))

cdf = [probabilites[0]]
for i in range(1,size):
    cdf.append(cdf[i-1]+probabilites[i])


print(probabilites)
print(cdf)
selected = []  #Array of selected columns from the original matrix

for i in range(0,c):
    rn = np.random.random()
    for j in range(len(cdf)):
        if(cdf[j]>rn):
            selected.append(j)
            break


approx_a = np.empty([c,size])  #The approximate matrix


for i in range(c):
    scale = c*probabilites[i]
    scale = math.sqrt(scale)
    approx_a[i] = mATrans[selected[i]]/scale

approx_a = np.asmatrix(approx_a)
approx_a = np.matrix.transpose(approx_a)
print("The new matrix is: ")
print(approx_a)
print
approx_a = np.asanyarray(approx_a)

print
print
print


pU, ps, pV = np.linalg.svd(approx_a, full_matrices=False)

print(np.shape(pV))

print("The new matrices U, s, V are :")

print
print

with printoptions(precision=2, suppress=True):
    print(pU)

print("\n")

with printoptions(precision=2, suppress=True):
    print(np.diag(ps))

print("\n")

with printoptions(precision=2, suppress=True):
    print(pV)
