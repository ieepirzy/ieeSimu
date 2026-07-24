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

# Parameterize the plane directly from its spanning vectors (point = P0 + s*v1 + t*v2)
# rather than solving for Z given X,Y, since that breaks down for vertical planes.
s = np.linspace(-10, 10, 20)
t = np.linspace(-10, 10, 20)
S, T = np.meshgrid(s, t)

X = P0[0] + S*v1[0] + T*v2[0]
Y = P0[1] + S*v1[1] + T*v2[1]
Z = P0[2] + S*v1[2] + T*v2[2]


# --- plotting ---
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.plot_surface(X, Y, Z, alpha=0.3)
ax.scatter(*P0, color='red')
ax.scatter(*P1, color='red')
ax.scatter(*P2, color='red')
plt.show()
