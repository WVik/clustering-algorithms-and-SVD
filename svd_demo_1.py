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


a = np.array([[0,1,1,0,1,0,0,0,0,0,0,1], [0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,1,0,0,0,0,0,0,0], [0,1,0,0,1,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0], [0,0,1,0,1,0,0,0,0,0,0,0], [0,1,1,0,0,0,0,0,0,0,0,1], [0,1,0,0,1,0,0,0,1,1,1,0], [0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,1,0,1,0,1,0], [0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0]])


u,s,v = np.linalg.svd(a, full_matrices=False,compute_uv=1)

with printoptions(precision=2, suppress=True):
    print(u)
print

with printoptions(precision=2, suppress=True):
    print(v)

print

with printoptions(precision=2, suppress=True):
    print(np.diag(s))

print(a)