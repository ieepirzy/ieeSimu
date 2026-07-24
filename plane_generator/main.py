# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 16:42:49 2026

"""
import matplotlib.pyplot as plt
import numpy as np

P0 = np.random.randint(1, 10, size=3)
P1 = np.random.randint(1, 10, size=3)
P2 = np.random.randint(1, 10, size=3)

v1 = P1-P0
v2 = P2-P0

n = np.cross(v1,v2)

A, B, C = n

D = np.dot(n, P0)

X = np.linspace(-200,200)
Y = np.linspace(-200,200)
Z = np.linspace(-200,200)

x = np.linspace(-10, 10, 20)
y = np.linspace(-10, 10, 20)
X, Y = np.meshgrid(x, y)

if C != 0:
    Z = (D - A*X - B*Y) / C
else:
    Z = np.zeros_like(X)


# --- plotting ---
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.plot_surface(X, Y, Z, alpha=0.3)
ax.scatter(*P0, color='red')
ax.scatter(*P1, color='red')
ax.scatter(*P2, color='red')
plt.show()
