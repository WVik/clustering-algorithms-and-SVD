from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
import random


fig = pyplot.figure()
ax = Axes3D(fig)

sequence_containing_x_vals = list([1,2,3,5,6])
sequence_containing_y_vals = list([1,2,3,5,6])
sequence_containing_z_vals = list([1,2,3,5,6])

ax.scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals)
pyplot.show()