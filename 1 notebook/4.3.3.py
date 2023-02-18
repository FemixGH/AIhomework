import numpy as np
import matplotlib.pyplot as plt
from numpy import trapz
x = np.arange(1, 9, 0.1)
y = np.abs(np.cos(x * (np.e ** np.cos(x) + np.log(x + 1))))
plt.grid()      #сетка графика
plt.plot(x, y, c = "black")
plt.fill_between(x, y)
area = trapz(y)
print(area)