import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(1.0, 2.0, 0.01)
s = t*2

# Note that using plt.subplots below is equivalent to using
# fig = plt.figure and then ax = fig.add_subplot(111)
fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='0 (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

fig.savefig("test.png")
plt.show()



