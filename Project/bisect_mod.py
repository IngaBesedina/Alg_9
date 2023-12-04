import timeit as ti
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

my_setup = """
from __main__ import a
from __main__ import search
import bisect
"""


def log_func(x, a, b):
    return a + b * np.log(x)


N = 5000
x = np.array(range(10, N + 1, 10))
y = []

for n in range(10, N + 1, 10):
    a = np.array(np.random.randint(-100, 100, n))
    a.sort()
    search = a[5]
    y.append(ti.timeit(setup=my_setup, stmt="bisect.bisect_left(a, search)", number=30))

popt, pcov = curve_fit(log_func, x, y)
a_opt, b_opt = popt
x_fit = np.linspace(min(x), max(x), 100)
y_fit = log_func(x_fit, a_opt, b_opt)

plt.scatter(x, y, s=5, color="b")
plt.plot(x_fit, y_fit, color="r")
plt.xlabel("Размер массива")
plt.ylabel("Время работы функции")
plt.title("Средний случай")
plt.show()
