import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as opt
from functools import partial
from math import *

events = {'A1': 0, 'A2': 1, 'B1': 2, 'B2': 3, 'C': 4, 'D1': 5, 'D2': 6, 'E': 7 }
l = np.array([0.0007, 0.0007, 0.0025, 0.0001, 0.00295, 0.0005, 0.00385, 0.00325])

def P(t, l, index):
    return 1-np.exp(-l[index] * t)

# A1 = lambda t: P(0,t)

# P = lambda(index, t): 1-exp(l[index] * t)

T = 500

for i in range(len(l)):
    print("\n" + str(P(T, l, i)))

def P_union2(t, l, index_1, index_2):
    return P(t, l, index_1) + P(t, l, index_2) - P(t, l, index_1) * P(t, l, index_2)

def P_union2P(P1, P2):
    return P1 + P2 - P1 * P2

def P_union3(t, l, index_1, index_2, index_3):
    return 1 - (1 - P(t, l, index_1)) * (1 - P(t, l, index_2)) * (1 - P(t, l, index_3))

def P_union3P(P1, P2, P3):
    return 1 - (1 - P1) * (1 - P2) * (1 - P3)

def P_inresection(t, l, *indeces):
    res = 1
    for i in indeces:
        res *= P(t, l, i)
    return res

D1uE = P_union2(T, l, events['D1'], events['E'])
print("\nD1uE =", D1uE)
D2uE = P_union2(T, l, events['D2'], events['E'])
print("D2uE =", D2uE)
CiB1iA1 = P_inresection(T, l, events['C'], events['B1'], events['A1'])
print("CiB1iA1 =", CiB1iA1)
CiB2iA2 = P_inresection(T, l, events['C'], events['B2'], events['A2'])
print("CiB2iA2 =", CiB2iA2)
hack_contour = P_union2P(CiB1iA1, CiB2iA2)
print("hack_contour =", hack_contour)
hack = P_union3P(P(T, l, events['E']), CiB1iA1, CiB2iA2)
print("hack =", hack)

def hack_t (l, t):
    CiB1iA1 = P_inresection(t, l, events['C'], events['B1'], events['A1'])
    CiB2iA2 = P_inresection(t, l, events['C'], events['B2'], events['A2'])
    return P_union3P(P(t, l, events['E']), CiB1iA1, CiB2iA2)

hack_t_bounded = partial(hack_t, l)

trange = np.arange(0.0,1000.0,0.1)
plt.plot(trange, hack_t_bounded(trange))
plt.show()

max_ind = events['E']
l_new = l.copy()
l_new[max_ind] /= 4

hack_t_bounded1 = partial(hack_t,l_new)

plt.plot(trange, hack_t_bounded1(trange))
plt.show()

def hack_multuplier(mult):
    return np.array([hack_t(l * m, T) for m in mult])


trange1 = np.arange(0.0,1.0,0.0001)
plt.plot(trange1, hack_multuplier(trange1))
plt.show()

hack1 = hack_t(l, T)

def to_opt(mult):
    return hack_multuplier([mult])[0] - hack1 / 2

x0 = opt.bisect(to_opt, 0, 1)
print("\n" + str(x0))
